import ast
import inspect
import logging
import os
import platform
import subprocess
import sys
from enum import Enum
from typing import Any, AnyStr, Dict, List, Tuple, Union, get_args, get_origin

import qdarkstyle
from faker import Faker
from faker_file.providers.bin_file import BinFileProvider
from faker_file.providers.bmp_file import (
    BmpFileProvider,
    GraphicBmpFileProvider,
)
from faker_file.providers.csv_file import CsvFileProvider
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.eml_file import EmlFileProvider
from faker_file.providers.epub_file import EpubFileProvider
from faker_file.providers.gif_file import (
    GifFileProvider,
    GraphicGifFileProvider,
)
from faker_file.providers.ico_file import (
    GraphicIcoFileProvider,
    IcoFileProvider,
)
from faker_file.providers.jpeg_file import (
    GraphicJpegFileProvider,
    JpegFileProvider,
)
from faker_file.providers.json_file import JsonFileProvider
from faker_file.providers.mixins.image_mixin import (
    IMAGEKIT_IMAGE_GENERATOR,
    PIL_IMAGE_GENERATOR,
    WEASYPRINT_IMAGE_GENERATOR,
)
from faker_file.providers.mp3_file import (
    EDGE_TTS_MP3_GENERATOR,
    GTTS_MP3_GENERATOR,
    Mp3FileProvider,
)
from faker_file.providers.odp_file import OdpFileProvider
from faker_file.providers.ods_file import OdsFileProvider
from faker_file.providers.odt_file import OdtFileProvider
from faker_file.providers.pdf_file import (
    PDFKIT_PDF_GENERATOR,
    PIL_PDF_GENERATOR,
    REPORTLAB_PDF_GENERATOR,
    GraphicPdfFileProvider,
    PdfFileProvider,
)
from faker_file.providers.png_file import (
    GraphicPngFileProvider,
    PngFileProvider,
)
from faker_file.providers.pptx_file import PptxFileProvider
from faker_file.providers.rtf_file import RtfFileProvider
from faker_file.providers.svg_file import SvgFileProvider
from faker_file.providers.tar_file import TarFileProvider
from faker_file.providers.tiff_file import (
    GraphicTiffFileProvider,
    TiffFileProvider,
)
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.providers.webp_file import (
    GraphicWebpFileProvider,
    WebpFileProvider,
)
from faker_file.providers.xlsx_file import XlsxFileProvider
from faker_file.providers.xml_file import XmlFileProvider
from faker_file.providers.zip_file import ZipFileProvider
from faker_file.storages.filesystem import FileSystemStorage
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QComboBox,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

__title__ = "faker-file-qt"
__version__ = "0.1.4"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "FakerFileApp",
    "get_item_key",
    "get_label_text",
    "main",
    "open_file_with_default_app",
    "str_to_type",
)

LOGGER = logging.getLogger(__name__)
FAKER = Faker()

KWARGS_DROP = {
    "self",  # Drop as irrelevant
    "storage",  # Drop as non-supported arg
    "return",  # Drop as irrelevant
    "format_func",  # Drop as non-supported arg
    "raw",  # Drop `raw`, because we will be forcing raw=True for streaming
}

OVERRIDES = {
    "DocxFileProvider.docx_file": {
        "annotations": {
            "content": str,
        },
        "model_props": {
            "content": None,
        },
    },
    # "Mp3FileProvider.mp3_file": {
    #     "annotations": {
    #         "mp3_generator_cls": str,
    #     },
    #     "model_props": {
    #         "mp3_generator_cls": GTTS_MP3_GENERATOR,
    #     },
    # },
    "OdtFileProvider.odt_file": {
        "annotations": {
            "content": str,
        },
        "model_props": {
            "content": None,
        },
    },
    # "PdfFileProvider.pdf_file": {
    #     "annotations": {
    #         "pdf_generator_cls": str,
    #     },
    #     "model_props": {
    #         "pdf_generator_cls": PDFKIT_PDF_GENERATOR,
    #     },
    # },
}


class PdfGeneratorCls(str, Enum):
    PIL_PDF_GENERATOR = PIL_PDF_GENERATOR
    REPORTLAB_PDF_GENERATOR = REPORTLAB_PDF_GENERATOR
    PDFKIT_PDF_GENERATOR = PDFKIT_PDF_GENERATOR


class ImageGeneratorCls(str, Enum):
    PIL_IMAGE_GENERATOR = PIL_IMAGE_GENERATOR
    IMAGEKIT_IMAGE_GENERATOR = IMAGEKIT_IMAGE_GENERATOR
    WEASYPRINT_IMAGE_GENERATOR = WEASYPRINT_IMAGE_GENERATOR


class ImagekitImageGeneratorCls(str, Enum):
    # PIL_IMAGE_GENERATOR = PIL_IMAGE_GENERATOR
    IMAGEKIT_IMAGE_GENERATOR = IMAGEKIT_IMAGE_GENERATOR
    # WEASYPRINT_IMAGE_GENERATOR = WEASYPRINT_IMAGE_GENERATOR


class WeasyprintImageGeneratorCls(str, Enum):
    # PIL_IMAGE_GENERATOR = PIL_IMAGE_GENERATOR
    # IMAGEKIT_IMAGE_GENERATOR = IMAGEKIT_IMAGE_GENERATOR
    WEASYPRINT_IMAGE_GENERATOR = WEASYPRINT_IMAGE_GENERATOR


class PilImageGeneratorCls(str, Enum):
    PIL_IMAGE_GENERATOR = PIL_IMAGE_GENERATOR
    # IMAGEKIT_IMAGE_GENERATOR = IMAGEKIT_IMAGE_GENERATOR
    # WEASYPRINT_IMAGE_GENERATOR = WEASYPRINT_IMAGE_GENERATOR


class ImagekitAndPilImageGeneratorCls(str, Enum):
    PIL_IMAGE_GENERATOR = PIL_IMAGE_GENERATOR
    IMAGEKIT_IMAGE_GENERATOR = IMAGEKIT_IMAGE_GENERATOR
    # WEASYPRINT_IMAGE_GENERATOR = WEASYPRINT_IMAGE_GENERATOR


class WeasyprintAndPilImageGeneratorCls(str, Enum):
    PIL_IMAGE_GENERATOR = PIL_IMAGE_GENERATOR
    # IMAGEKIT_IMAGE_GENERATOR = IMAGEKIT_IMAGE_GENERATOR
    WEASYPRINT_IMAGE_GENERATOR = WEASYPRINT_IMAGE_GENERATOR


class Mp3GeneratorCls(str, Enum):
    GTTS_MP3_GENERATOR = GTTS_MP3_GENERATOR
    EDGE_TTS_MP3_GENERATOR = EDGE_TTS_MP3_GENERATOR


SELECTS = {
    "pdf_generator_cls": {
        PdfFileProvider.pdf_file.__name__: [
            __i.value for __i in PdfGeneratorCls
        ],
    },
    "image_generator_cls": {
        BmpFileProvider.bmp_file.__name__: [
            __i.value for __i in WeasyprintAndPilImageGeneratorCls
        ],
        GifFileProvider.gif_file.__name__: [
            __i.value for __i in WeasyprintAndPilImageGeneratorCls
        ],
        IcoFileProvider.ico_file.__name__: [
            __i.value for __i in ImagekitImageGeneratorCls
        ],
        JpegFileProvider.jpeg_file.__name__: [
            __i.value for __i in ImageGeneratorCls
        ],
        PngFileProvider.png_file.__name__: [
            __i.value for __i in ImageGeneratorCls
        ],
        SvgFileProvider.svg_file.__name__: [
            __i.value for __i in ImagekitImageGeneratorCls
        ],
        TiffFileProvider.tiff_file.__name__: [
            __i.value for __i in WeasyprintAndPilImageGeneratorCls
        ],
        WebpFileProvider.webp_file.__name__: [
            __i.value for __i in ImageGeneratorCls
        ],
    },
    "mp3_generator_cls": {
        Mp3FileProvider.mp3_file.__name__: [
            __i.value for __i in Mp3GeneratorCls
        ],
    },
}


PROVIDERS = {
    BinFileProvider.bin_file.__name__: BinFileProvider,
    BmpFileProvider.bmp_file.__name__: BmpFileProvider,
    CsvFileProvider.csv_file.__name__: CsvFileProvider,
    DocxFileProvider.docx_file.__name__: DocxFileProvider,
    EmlFileProvider.eml_file.__name__: EmlFileProvider,
    EpubFileProvider.epub_file.__name__: EpubFileProvider,
    GifFileProvider.gif_file.__name__: GifFileProvider,
    GraphicBmpFileProvider.graphic_bmp_file.__name__: GraphicBmpFileProvider,
    GraphicGifFileProvider.graphic_gif_file.__name__: GraphicGifFileProvider,
    GraphicIcoFileProvider.graphic_ico_file.__name__: GraphicIcoFileProvider,
    GraphicJpegFileProvider.graphic_jpeg_file.__name__: (
        GraphicJpegFileProvider
    ),
    GraphicPdfFileProvider.graphic_pdf_file.__name__: GraphicPdfFileProvider,
    GraphicPngFileProvider.graphic_png_file.__name__: GraphicPngFileProvider,
    GraphicTiffFileProvider.graphic_tiff_file.__name__: GraphicTiffFileProvider,
    GraphicWebpFileProvider.graphic_webp_file.__name__: (
        GraphicWebpFileProvider
    ),
    IcoFileProvider.ico_file.__name__: IcoFileProvider,
    JpegFileProvider.jpeg_file.__name__: JpegFileProvider,
    JsonFileProvider.json_file.__name__: JsonFileProvider,
    Mp3FileProvider.mp3_file.__name__: Mp3FileProvider,
    OdpFileProvider.odp_file.__name__: OdpFileProvider,
    OdsFileProvider.ods_file.__name__: OdsFileProvider,
    OdtFileProvider.odt_file.__name__: OdtFileProvider,
    PdfFileProvider.pdf_file.__name__: PdfFileProvider,
    PngFileProvider.png_file.__name__: PngFileProvider,
    PptxFileProvider.pptx_file.__name__: PptxFileProvider,
    RtfFileProvider.rtf_file.__name__: RtfFileProvider,
    SvgFileProvider.svg_file.__name__: SvgFileProvider,
    TarFileProvider.tar_file.__name__: TarFileProvider,
    TiffFileProvider.tiff_file.__name__: TiffFileProvider,
    TxtFileProvider.txt_file.__name__: TxtFileProvider,
    WebpFileProvider.webp_file.__name__: WebpFileProvider,
    XlsxFileProvider.xlsx_file.__name__: XlsxFileProvider,
    XmlFileProvider.xml_file.__name__: XmlFileProvider,
    ZipFileProvider.zip_file.__name__: ZipFileProvider,
}

STORAGE = FileSystemStorage()

# Names that should show a multi-line text box
MULTI_LINE_INPUTS = [
    "content",
    "data_columns",
    "options",
    "mp3_generator_kwargs",
    "pdf_generator_kwargs",
]


def str_to_type(s: str, t: type) -> Any:
    if t in {int, float}:
        return t(s)
    elif t is bool:
        return bool(s)
    elif t is str:
        return s
    elif t is bytes:
        return s.encode()
    elif t in {AnyStr, Any}:
        return s  # Just return the string
    elif get_origin(t) is Union:
        args = get_args(t)
        if type(None) in args:
            # It's an Optional type
            for arg in args:
                if arg is not type(None):  # Try the other type
                    if s:  # If the string is not empty, try to convert
                        return str_to_type(s, arg)
                    else:  # If the string is empty, return None
                        return None
        elif bytes in args and str in args:  # Special case: Union[bytes, str]
            try:
                return s.encode()  # Try to decode as bytes first
            except UnicodeDecodeError:  # If that fails, return as str
                return s
        else:
            raise NotImplementedError(f"Don't know how to handle {t}")
    else:
        origin = get_origin(t)
        if origin in {list, List}:
            return [str_to_type(x, get_args(t)[0]) for x in ast.literal_eval(s)]
        elif origin in {tuple, Tuple}:
            return tuple(
                str_to_type(x, get_args(t)[0]) for x in ast.literal_eval(s)
            )
        elif origin in {dict, Dict}:
            return {
                k: str_to_type(v, get_args(t)[1])
                for k, v in ast.literal_eval(s).items()
            }
        else:
            raise NotImplementedError(f"Don't know how to handle {t}")


def get_label_text(name: str) -> str:
    return name.replace("_file", "").replace("_", " ")


def get_item_key(item) -> str:
    return item.data(QtCore.Qt.UserRole)


def open_file_with_default_app(file_path: str) -> None:
    """Open file with default app.

    Example usage:

        open_file_with_default_app("/path/to/the/file.ext")
    """
    if platform.system() == "Darwin":  # macOS
        subprocess.run(("open", file_path))
    elif platform.system() == "Windows":  # Windows
        subprocess.run(("start", file_path), shell=True)
    else:  # linux variants
        subprocess.run(("xdg-open", file_path))


class FakerFileApp(QMainWindow):
    def __init__(self: "FakerFileApp") -> None:
        super().__init__()

        # Initialize
        self.param_widgets = {}
        self.param_annotations = {}
        self.initUI()

    def initUI(self: "FakerFileApp") -> None:
        # Set window size
        self.setGeometry(200, 200, 960, 720)

        # Create menu bar
        menu_bar = self.menuBar()

        # Create menus
        file_menu = menu_bar.addMenu("&File")
        help_menu = menu_bar.addMenu("&Help")

        browse_files_action = QAction("&Browse Files", self)
        browse_files_action.setStatusTip(
            "Open storage location using default file browser"
        )
        browse_files_action.triggered.connect(self.browse_files_menu_action)

        about_action = QAction("&About", self)
        about_action.setStatusTip(f"About {__title__}")
        about_action.triggered.connect(self.about_message_menu_action)

        # Add actions to menus
        file_menu.addAction(browse_files_action)
        help_menu.addAction(about_action)

        # Create a QHBoxLayout
        layout = QHBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.show_form)
        list_group = QGroupBox("File type")  # create a group box
        list_layout = QVBoxLayout()  # create a layout for the group box
        list_layout.addWidget(self.list_widget)
        list_group.setLayout(list_layout)

        self.form_widget = QWidget()
        self.form_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.form_layout = QFormLayout(self.form_widget)
        self.form_layout.setContentsMargins(
            10, 10, 10, 10
        )  # set some margins for spacing
        form_group = QGroupBox("Options")  # create a group box
        form_layout = QVBoxLayout()  # create a layout for the group box
        form_layout.addWidget(self.form_widget)
        form_layout.addStretch(1)  # Add stretch to bottom
        form_group.setLayout(form_layout)

        self.result_widget = QListWidget()
        self.result_widget.itemDoubleClicked.connect(
            self.handle_result_item_click
        )
        result_group = QGroupBox("Results")  # create a group box
        result_layout = QVBoxLayout()  # create a layout for the group box
        result_layout.addWidget(self.result_widget)
        result_group.setLayout(result_layout)

        for file_type in PROVIDERS.keys():
            list_item = QListWidgetItem(get_label_text(file_type))
            # Store the original string in the UserRole data role
            list_item.setData(QtCore.Qt.UserRole, file_type)
            self.list_widget.addItem(list_item)

        self.list_widget.setCurrentRow(0)
        self.list_widget.itemClicked.emit(self.list_widget.currentItem())

        layout.addWidget(list_group, -1)
        layout.addWidget(form_group, 3)
        layout.addWidget(result_group, 3)
        self.setLayout(layout)

        self.setCentralWidget(
            QWidget()
        )  # QMainWindow requires a central widget
        self.centralWidget().setLayout(layout)

    def about_message_menu_action(self):
        QMessageBox.about(
            self,
            f"About {__title__}",
            (
                f"{__title__} version {__version__}.\n\n"
                f"Author: {__author__}\n"
                f"License: {__license__}\n"
            ),
        )

    def browse_files_menu_action(self):
        open_file_with_default_app(
            os.path.join(STORAGE.root_path, STORAGE.rel_path)
        )

    def show_form(self: "FakerFileApp", item: "QListWidgetItem") -> None:
        file_type = get_item_key(item)
        provider = PROVIDERS[file_type]

        method = getattr(provider(FAKER), file_type)
        method_specs = inspect.getfullargspec(method)

        # Clear the form
        for i in reversed(range(self.form_layout.count())):
            self.form_layout.itemAt(i).widget().deleteLater()

        self.param_widgets = {}  # Clear the value
        self.param_annotations = {}  # Clear the value

        # Build the form
        for arg in method_specs.args[1:]:  # Omit 'self'
            if arg not in KWARGS_DROP:
                label = QLabel(get_label_text(arg))

                if arg in SELECTS:
                    combo_box = QComboBox()
                    combo_box.addItems(SELECTS[arg][file_type])
                    self.form_layout.addWidget(label)
                    self.form_layout.addWidget(combo_box)
                    self.param_widgets[arg] = combo_box
                    combo_box.setSizePolicy(
                        QSizePolicy.Expanding, QSizePolicy.Fixed
                    )
                    combo_box.setFixedWidth(300)
                else:
                    line_edit = (
                        QTextEdit() if arg in MULTI_LINE_INPUTS else QLineEdit()
                    )
                    line_edit.setSizePolicy(
                        QSizePolicy.Expanding, QSizePolicy.Fixed
                    )
                    line_edit.setFixedWidth(300)

                    self.form_layout.addWidget(label)
                    self.form_layout.addWidget(line_edit)

                    # Store a reference to the widget
                    self.param_widgets[arg] = line_edit

                self.param_annotations[arg] = method_specs.annotations.get(
                    arg, str
                )  # Store the type annotation

        generate_button = QPushButton("Generate")
        generate_button.clicked.connect(self.generate_result)
        self.form_layout.addWidget(generate_button)

    def generate_result(self: "FakerFileApp") -> None:
        kwargs = {}

        # Extract the values from the QLineEdit widgets and convert them to
        # their appropriate types.
        for param, widget in self.param_widgets.items():
            if isinstance(widget, QComboBox):
                input_value = widget.currentText().strip()
            elif isinstance(widget, QTextEdit):
                input_value = widget.toPlainText().strip()
            elif isinstance(widget, QLineEdit):
                input_value = widget.text().strip()
            else:
                input_value = None
            type_annotation = self.param_annotations[param]

            # If the input value is not empty, convert it to its appropriate
            # type.
            if input_value:
                converted_value = str_to_type(input_value, type_annotation)
            else:  # If the input value is empty, use None
                converted_value = None
            if input_value:
                kwargs[param] = converted_value

        # Handle the overrides
        for key, value in OVERRIDES.items():
            provider_key, method_name = key.split(".")
            if get_item_key(self.list_widget.currentItem()) == method_name:
                if "model_props" in value and value["model_props"]:
                    kwargs.update(value["model_props"])

        file_type = get_item_key(self.list_widget.currentItem())
        provider = PROVIDERS[file_type]
        method = getattr(provider(FAKER), file_type)

        try:
            result = method(**kwargs)  # Get your result here
            result_text = result.data["filename"]
        except Exception as err:
            LOGGER.debug(kwargs)
            LOGGER.exception(err)
            result = None
            result_text = ""

        self.result_widget.addItem(str(result_text))  # Display the result
        self.result_widget.setCurrentRow(self.result_widget.count() - 1)

    def handle_result_item_click(
        self: "FakerFileApp", item: "QListWidgetItem"
    ) -> None:
        open_file_with_default_app(item.text())


def main() -> None:
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # app.setStyleSheet(
    #     qdarkstyle._load_stylesheet(
    #         qt_api='pyqt5',
    #         palette=qdarkstyle.light.palette.LightPalette,
    #     )
    # )
    ex = FakerFileApp()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
