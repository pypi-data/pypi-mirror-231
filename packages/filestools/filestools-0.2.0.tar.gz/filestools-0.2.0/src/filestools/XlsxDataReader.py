import datetime
import re
from zipfile import ZipFile

from defusedxml.ElementTree import iterparse
from lxml import etree
import posixpath


def _get_column_letter(col_idx):
    """Convert a column number into a column letter (3 -> 'C')

    Right shift the column col_idx by 26 to find column letters in reverse
    order.  These numbers are 1-based, and can be converted to ASCII
    ordinals by adding 64.

    """
    # these indicies corrospond to A -> ZZZ and include all allowed
    # columns
    if not 1 <= col_idx <= 18278:
        raise ValueError("Invalid column index {0}".format(col_idx))
    letters = []
    while col_idx > 0:
        col_idx, remainder = divmod(col_idx, 26)
        # check for exact division and borrow if needed
        if remainder == 0:
            remainder = 26
            col_idx -= 1
        letters.append(chr(remainder + 64))
    return ''.join(reversed(letters))


_COL_STRING_CACHE = {}
_STRING_COL_CACHE = {}
for i in range(1, 18279):
    col = _get_column_letter(i)
    _STRING_COL_CACHE[i] = col
    _COL_STRING_CACHE[col] = i


def get_column_letter(idx, ):
    """Convert a column index into a column letter
    (3 -> 'C')
    """
    try:
        return _STRING_COL_CACHE[idx]
    except KeyError:
        raise ValueError("Invalid column index {0}".format(idx))


def column_index_from_string(str_col):
    """Convert a column name into a numerical index
    ('A' -> 1)
    """
    # we use a function argument to get indexed name lookup
    try:
        return _COL_STRING_CACHE[str_col.upper()]
    except KeyError:
        raise ValueError("{0} is not a valid column name".format(str_col))


BUILTIN_FORMATS = {
    0: 'General', 1: '0', 2: '0.00', 3: '#,##0', 4: '#,##0.00', 5: '"$"#,##0_);("$"#,##0)',
    6: '"$"#,##0_);[Red]("$"#,##0)', 7: '"$"#,##0.00_);("$"#,##0.00)', 8: '"$"#,##0.00_);[Red]("$"#,##0.00)',
    9: '0%', 10: '0.00%', 11: '0.00E+00', 12: '# ?/?', 13: '# ??/??', 14: 'mm-dd-yy',
    15: 'd-mmm-yy', 16: 'd-mmm', 17: 'mmm-yy', 18: 'h:mm AM/PM',
    19: 'h:mm:ss AM/PM', 20: 'h:mm', 21: 'h:mm:ss', 22: 'm/d/yy h:mm',

    37: '#,##0_);(#,##0)', 38: '#,##0_);[Red](#,##0)', 39: '#,##0.00_);(#,##0.00)', 40: '#,##0.00_);[Red](#,##0.00)',

    41: r'_(* #,##0_);_(* \(#,##0\);_(* "-"_);_(@_)',
    42: r'_("$"* #,##0_);_("$"* \(#,##0\);_("$"* "-"_);_(@_)',
    43: r'_(* #,##0.00_);_(* \(#,##0.00\);_(* "-"??_);_(@_)',

    44: r'_("$"* #,##0.00_)_("$"* \(#,##0.00\)_("$"* "-"??_)_(@_)',
    45: 'mm:ss', 46: '[h]:mm:ss', 47: 'mmss.0', 48: '##0.0E+0', 49: '@',
}

ARC_CORE = 'docProps/core.xml'
PACKAGE_RELS = '_rels'
ARC_THEME = f'xl/theme/theme1.xml'
ARC_STYLE = f'xl/styles.xml'
ARC_CONTENT_TYPES = '[Content_Types].xml'
SHEET_MAIN_NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
INLINE_STRING = "{%s}is" % SHEET_MAIN_NS
ROW_TAG = '{%s}row' % SHEET_MAIN_NS
VALUE_TAG = '{%s}v' % SHEET_MAIN_NS
SECS_PER_DAY = 24 * 60 * 60
WINDOWS_EPOCH = datetime.datetime(1899, 12, 30)
MAC_EPOCH = datetime.datetime(1904, 1, 1)
LITERAL_GROUP = r'".*?"'  # anything in quotes
LOCALE_GROUP = r'\[(?!hh?\]|mm?\]|ss?\])[^\]]*\]'  # anything in square brackets, except hours or minutes or seconds
STRIP_RE = re.compile(f"{LITERAL_GROUP}|{LOCALE_GROUP}")
ISO_REGEX = re.compile(r'''
(?P<date>(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}))?T?
(?P<time>(?P<hour>\d{2}):(?P<minute>\d{2})(:(?P<second>\d{2})(?P<microsecond>\.\d{1,3})?)?)?Z?''',
                       re.VERBOSE)
ISO_DURATION = re.compile(r'PT((?P<hours>\d+)H)?((?P<minutes>\d+)M)?((?P<seconds>\d+(\.\d{1,3})?)S)?')


def from_ISO8601(formatted_string):
    if not formatted_string:
        return None

    match = ISO_REGEX.match(formatted_string)
    if match and any(match.groups()):
        parts = match.groupdict(0)
        for key in ["year", "month", "day", "hour", "minute", "second"]:
            if parts[key]:
                parts[key] = int(parts[key])

        if parts["microsecond"]:
            parts["microsecond"] = int(float(parts['microsecond']) * 1_000_000)

        if not parts["date"]:
            dt = datetime.time(parts['hour'], parts['minute'], parts['second'], parts["microsecond"])
        elif not parts["time"]:
            dt = datetime.date(parts['year'], parts['month'], parts['day'])
        else:
            del parts["time"]
            del parts["date"]
            dt = datetime.datetime(**parts)
        return dt

    match = ISO_DURATION.match(formatted_string)
    if match and any(match.groups()):
        parts = match.groupdict(0)
        for key, val in parts.items():
            if val:
                parts[key] = float(val)
        return datetime.timedelta(**parts)

    raise ValueError("Invalid datetime value {}".format(formatted_string))


class XlsxDataReader:
    def __init__(self, filename, unknownIsDate=True):
        self.archive = ZipFile(filename, 'r')
        self.valid_files = self.archive.namelist()
        self.manifest = self.read_manifest()
        self.shared_strings = self.read_strings()
        self.workbook_part_name = self.find_workbook_part_name()
        self.read_epoch()
        self.rels = self.get_dependents(self.workbook_part_name)
        self.read_sheet_name()
        self.unknownIsDate = unknownIsDate
        self.read_date_formats()

    def read_epoch(self):
        src = self.archive.read(self.workbook_part_name)
        node = etree.fromstring(src)
        workbookPr = node.xpath("./x:workbookPr", namespaces={"x": SHEET_MAIN_NS})[0].attrib
        self.epoch = WINDOWS_EPOCH
        if "date1904" in workbookPr and workbookPr["date1904"]:
            self.epoch = MAC_EPOCH

    def read_date_formats(self):
        node = etree.fromstring(self.archive.read(ARC_STYLE))
        self.numFmts = {
            int(el.get("numFmtId")): el.get("formatCode") for el in node.xpath(
                "x:numFmts/x:numFmt", namespaces={"x": SHEET_MAIN_NS})
        }
        self.date_formats = set()
        cell_styles = node.xpath("x:cellXfs/x:xf", namespaces={"x": SHEET_MAIN_NS})
        for idx, el in enumerate(cell_styles):
            style = el.attrib
            numFmtId = int(style["numFmtId"])
            if numFmtId in self.numFmts:
                fmt = self.numFmts[numFmtId]
            else:
                fmt = BUILTIN_FORMATS.get(numFmtId)
            if fmt is not None:
                fmt = fmt.split(";")[0]
                if re.search(r"[^\\][dmhysDMHYS]", STRIP_RE.sub("", fmt)) is not None:
                    self.date_formats.add(idx)
            elif self.unknownIsDate:
                self.date_formats.add(idx)
        self.bookViews = [el.attrib for el in node.xpath(
            "x:bookViews/x:workbookView", namespaces={"x": SHEET_MAIN_NS})]

    def read_sheet_name(self):
        src = self.archive.read(self.workbook_part_name)
        node = etree.fromstring(src)
        self.sheets = [{self.local_name(k): v for k, v in el.attrib.items()} for el in node.xpath(
            "x:sheets/x:sheet", namespaces={"x": SHEET_MAIN_NS})]
        name2file = {}
        for sheet in self.sheets:
            name2file[sheet["name"]] = self.rels[sheet["id"]]["Target"]
        self.name2file = name2file

    @property
    def active(self):
        for view in self.bookViews:
            if "activeTab" in view:
                return int(view["activeTab"])
        return 0

    @staticmethod
    def local_name(name):
        NS_REGEX = "({(?P<namespace>.*)})?(?P<localname>.*)"
        return re.match(NS_REGEX, name).group('localname')

    @staticmethod
    def get_rels_path(path):
        folder, obj = posixpath.split(path)
        filename = posixpath.join(folder, '_rels', '{0}.rels'.format(obj))
        return filename

    def from_excel_time(self, value):
        SECS_PER_DAY = 24 * 60 * 60
        day, fraction = divmod(value, 1)
        diff = datetime.timedelta(
            milliseconds=round(fraction * SECS_PER_DAY * 1000))
        if 0 <= value < 1 and diff.days == 0:
            mins, seconds = divmod(diff.seconds, 60)
            hours, mins = divmod(mins, 60)
            dt = datetime.time(hours, mins, seconds, diff.microseconds)
        else:
            if 0 < value < 60 and self.epoch == WINDOWS_EPOCH:
                day += 1
            dt = self.epoch + datetime.timedelta(days=day) + diff
        return dt

    def read_manifest(self):
        src = self.archive.read(ARC_CONTENT_TYPES)
        manifest = {}
        for el in etree.fromstring(src):
            manifest.setdefault(self.local_name(el.tag), []).append(el.attrib)
        return manifest

    def read_strings(self):
        ct = None
        SHARED_STRINGS = "application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"
        for t in self.manifest["Override"]:
            if t["ContentType"] == SHARED_STRINGS:
                ct = t
                break
        shared_strings = []
        if ct is not None:
            strings_path = ct["PartName"][1:]
            root = etree.fromstring(self.archive.read(strings_path))
            for node in root.xpath("//x:si", namespaces={"x": SHEET_MAIN_NS}):
                snippets = node.xpath(".//x:t/text()", namespaces={"x": SHEET_MAIN_NS})
                shared_strings.append("".join(snippets).replace('x005F_', ''))
        return shared_strings

    def find_workbook_part_name(self):
        WORKBOOK_MACRO = "application/vnd.ms-excel.{}.macroEnabled.main+xml"
        WORKBOOK = "application/vnd.openxmlformats-officedocument.spreadsheetml.{}.main+xml"
        XLTM = WORKBOOK_MACRO.format('template')
        XLSM = WORKBOOK_MACRO.format('sheet')
        XLTX = WORKBOOK.format('template')
        XLSX = WORKBOOK.format('sheet')
        for ct in (XLTM, XLTX, XLSM, XLSX):
            for t in self.manifest["Override"]:
                if t["ContentType"] == ct:
                    return t["PartName"][1:]

    def get_dependents(self, filename):
        filename = self.get_rels_path(filename)
        folder = posixpath.dirname(filename)
        parent = posixpath.split(folder)[0]
        rels = {}
        for el in etree.fromstring(self.archive.read(filename)):
            r = el.attrib
            if r.get("TargetMode") == "External":
                continue
            elif r["Target"].startswith("/"):
                r["Target"] = r["Target"][1:]
            else:
                pth = posixpath.join(parent, r["Target"])
                r["Target"] = posixpath.normpath(pth)
            rels[r.get("Id")] = r
        return rels

    @staticmethod
    def get_text_content(node):
        snippets = []
        plain = node.find("./x:t", namespaces={"x": SHEET_MAIN_NS})
        if plain is not None:
            snippets.append(plain.text)
        for t in node.findall("./x:r/x:t", namespaces={"x": SHEET_MAIN_NS}):
            snippets.append(t.text)
        return "".join(snippets)

    def parse_dimensions(self, worksheet_path):
        source = self.archive.open(worksheet_path)
        for _event, element in iterparse(source):
            tag_name = self.local_name(element.tag)
            if tag_name == "dimension":
                ref = element.get("ref")
                min_col, min_row, sep, max_col, max_row = re.match(
                    "\$?([A-Za-z]{1,3})\$?(\d+)(:\$?([A-Za-z]{1,3})\$?(\d+))?", ref).groups()
                min_col, max_col = map(
                    column_index_from_string, (min_col, max_col))
                min_row, max_row = map(int, (min_row, max_row))
                return min_col, min_row, max_col, max_row
            elif tag_name == "sheetData":
                break
            element.clear()
        source.close()

    def loadDataFromFile(self, file):
        min_col, min_row, max_col, max_row = self.parse_dimensions(file)
        src = self.archive.open(file)
        for _, element in iterparse(src):
            tag_name = element.tag
            if tag_name != ROW_TAG:
                continue
            cells = [None] * max_col
            flag = False
            for el in element:
                data_type = el.get('t', 'n')
                col_str, row_num = re.match("([A-Za-z]{1,3})(\d+)", el.get('r')).groups()
                col_num = column_index_from_string(col_str)
                style_id = int(el.get('s', 0))
                value = None
                if data_type == "inlineStr":
                    child = el.find(INLINE_STRING)
                    if child is not None:
                        # data_type = 's'
                        value = self.get_text_content(child)
                else:
                    value = el.findtext(VALUE_TAG, None)
                    if value is not None:
                        flag = True
                        if data_type == 'n':
                            if re.search("[.e]", value, flags=re.I):
                                value = float(value)
                            else:
                                value = int(value)
                            if style_id in self.date_formats:
                                # data_type = 'd'
                                try:
                                    value = self.from_excel_time(value)
                                except (OverflowError, ValueError):
                                    data_type = "e"
                                    # value = "#VALUE!"
                        elif data_type == 's':
                            value = self.shared_strings[int(value)]
                        elif data_type == 'b':
                            value = bool(int(value))
                        elif data_type == "str":
                            data_type = "s"
                        elif data_type == 'd':
                            value = from_ISO8601(value)
                # print(row_num, col_num, value)
                cells[col_num - 1] = value
            element.clear()
            if flag:
                yield cells
        src.close()

    def load_data(self, sheet_name=None, limit: int = None):
        if sheet_name is None:
            sheet_name = self.active
        if isinstance(sheet_name, int):
            if sheet_name >= len(self.sheets):
                raise Exception("索引不存在")
            sheet_name = self.sheets[sheet_name]["name"]
        if not isinstance(sheet_name, str):
            raise Exception("表名类型不正确")
        file = self.name2file[sheet_name]
        it = self.loadDataFromFile(file)
        if limit is not None:
            data = []
            for line in it:
                data.append(line)
                limit -= 1
                if limit <= 0:
                    break
            return data
        return it

    def sheet_names(self):
        return [row["name"] for row in self.sheets]
