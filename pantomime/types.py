from pantomime.util import gettext

DEFAULT = 'application/octet-stream'
DIRECTORY = 'inode/directory'
EMPTY = 'inode/x-empty'

PLAIN = 'text/plain'
PDF = 'application/pdf'
EXCEL = 'application/vnd.ms-excel'
WORD = 'application/vnd.ms-word'
CSV = 'text/csv'
RTF = 'text/rtf'
PSD = 'image/vnd.adobe.photoshop'
RAR = 'application/rar'
ZIP = 'application/zip'
GZIP = 'application/gzip'
RFC822 = 'message/rfc822'
HTML = 'text/html'
JPEG = 'image/jpeg'
PNG = 'image/png'
GIF = 'image/gif'
TIFF = 'image/tiff'
DJVU = 'image/x.djvu'
OPF = 'application/xml+opfmessage'


LABELS = {
    DEFAULT: gettext("Unknown file type"),
    DIRECTORY: gettext("Directory"),
    EMPTY: gettext("Empty file"),
    PLAIN: gettext("Plain text"),
    PDF: gettext("Portable Document Format"),
    EXCEL: gettext("Microsoft Excel"),
    WORD: gettext("Microsoft Word"),
    CSV: gettext("Comma-separated table"),
    RTF: gettext("Rich text"),
    PSD: gettext("Adobe Photoshop"),
    RAR: gettext("WinRAR Archive"),
    ZIP: gettext("Zip Archive"),
    GZIP: gettext("GZip Archive"),
    RFC822: gettext("Plain E-Mail"),
    HTML: gettext("HTML Web Page"),
    JPEG: gettext("JPEG Image"),
    TIFF: gettext("Tagged Image File Format"),
    DJVU: gettext("DejaVu E-Book"),
    PNG: gettext("Portable Nework Graphics"),
    GIF: gettext("Graphics Interchange Format"),
    OPF: gettext("Outlook for Mac E-Mail")
}
