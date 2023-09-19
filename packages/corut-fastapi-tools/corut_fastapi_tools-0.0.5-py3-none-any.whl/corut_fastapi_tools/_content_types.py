from typing import List

__all__ = (
    'ALL_TYPES',
    'APPS',
    'FONTS',
    'IMAGES',
    'SOUNDS',
    'TEXTS',
    'VIDEOS',
    'get_special_content_types',
)

APPS = {
    'epub': 'application/epub+zip',
    'gz': 'application/gzip',
    'jar': 'application/java-archive',
    'json': 'application/json',
    'jsonld': 'application/ld+json',
    'doc': 'application/msword',
    'bin': 'application/octet-stream',
    'ogx': 'application/ogg',
    'pdf': 'application/pdf',
    'rtf': 'application/rtf',
    'azw': 'application/vnd.amazon.ebook',
    'mpkg': 'application/vnd.apple.installer+xml',
    'xul': 'application/vnd.mozilla.xul+xml',
    'xls': 'application/vnd.ms-excel',
    'eot': 'application/vnd.ms-fontobject',
    'ppt': 'application/vnd.ms-powerpoint',
    'odp': 'application/vnd.oasis.opendocument.presentation',
    'ods': 'application/vnd.oasis.opendocument.spreadsheet',
    'odt': 'application/vnd.oasis.opendocument.text',
    'pptx': 'application/vnd.openxmlformats-officedocument.'
            'presentationml.presentation',
    'xlsx': 'application/vnd.openxmlformats-officedocument.'
            'spreadsheetml.sheet',
    'docx': 'application/vnd.openxmlformats-officedocument.'
            'wordprocessingml.document',
    'rar': 'application/vnd.rar',
    'vsd': 'application/vnd.visio',
    '7z': 'application/x-7z-compressed',
    'abw': 'application/x-abiword',
    'bz': 'application/x-bzip',
    'bz2': 'application/x-bzip2',
    'cda': 'application/x-cdf',
    'csh': 'application/x-csh',
    'arc': 'application/x-freearc',
    'php': 'application/x-httpd-php',
    'sh': 'application/x-sh',
    'tar': 'application/x-tar',
    'xhtml': 'application/xhtml+xml',
    'xml': 'application/xml',
    'zip': 'application/zip',
}
SOUNDS = {
    'aac': 'audio/aac',
    'mid': 'audio/midi',
    'midi': 'audio/x-midi',
    'mp3': 'audio/mpeg',
    'oga': 'audio/ogg',
    'opus': 'audio/opus',
    'wav': 'audio/wav',
    'wma': 'audio/x-ms-wma',
    'weba': 'audio/webm',
}
FONTS = {
    'otf': 'font/otf',
    'ttf': 'font/ttf',
    'woff': 'font/woff',
    'woff2': 'font/woff2',
}
IMAGES = {
    'avif': 'image/avif',
    'bmp': 'image/bmp',
    'gif': 'image/gif',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    'png': 'image/png',
    'svg': 'image/svg+xml',
    'tif': 'image/tiff',
    'tiff': 'image/tiff',
    'ico': 'image/vnd.microsoft.icon',
    'webp': 'image/webp',
}
TEXTS = {
    'ics': 'text/calendar',
    'css': 'text/css',
    'csv': 'text/csv',
    'htm': 'text/html',
    'html': 'text/html',
    'mjs': 'text/javascript',
    'js': 'text/javascript',
    'txt': 'text/plain',
}
VIDEOS = {
    '3gp': 'video/3gpp',
    '3g2': 'video/3gpp2',
    'ts': 'video/mp2t',
    'mp4': 'video/mp4',
    'mpeg': 'video/mpeg',
    'ogv': 'video/ogg',
    'webm': 'video/webm',
    'avi': 'video/x-msvideo',
}
ALL_TYPES: dict = {**APPS, **FONTS, **IMAGES, **SOUNDS, **TEXTS, **VIDEOS}


def get_special_content_types(types: List[str], data: dict = None) -> dict:
    if data is None:
        data = ALL_TYPES
    return {k: v for k, v in data if k in types}
