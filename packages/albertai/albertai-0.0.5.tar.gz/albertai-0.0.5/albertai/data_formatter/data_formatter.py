from albertai.chunkers.docs_site import DocsSiteChunker
from albertai.chunkers.docx_file import DocxFileChunker
from albertai.chunkers.notion import NotionChunker
from albertai.chunkers.pdf_file import PdfFileChunker
from albertai.chunkers.qna_pair import QnaPairChunker
from albertai.chunkers.text import TextChunker
from albertai.chunkers.web_page import WebPageChunker
from albertai.chunkers.youtube_video import YoutubeVideoChunker
from albertai.config import AddConfig
from albertai.loaders.docs_site_loader import DocsSiteLoader
from albertai.loaders.docx_file import DocxFileLoader
from albertai.loaders.local_qna_pair import LocalQnaPairLoader
from albertai.loaders.local_text import LocalTextLoader
from albertai.loaders.pdf_file import PdfFileLoader
from albertai.loaders.sitemap import SitemapLoader
from albertai.loaders.web_page import WebPageLoader
from albertai.loaders.youtube_video import YoutubeVideoLoader
from albertai.models.data_type import DataType


class DataFormatter:
    """
    DataFormatter is an internal utility class which abstracts the mapping for
    loaders and chunkers to the data_type entered by the user in their
    .add or .add_local method call
    """

    def __init__(self, data_type: DataType, config: AddConfig):
        self.loader = self._get_loader(data_type, config.loader)
        self.chunker = self._get_chunker(data_type, config.chunker)

    def _get_loader(self, data_type: DataType, config):
        """
        Returns the appropriate data loader for the given data type.

        :param data_type: The type of the data to load.
        :return: The loader for the given data type.
        :raises ValueError: If an unsupported data type is provided.
        """
        loaders = {
            DataType.YOUTUBE_VIDEO: YoutubeVideoLoader,
            DataType.PDF_FILE: PdfFileLoader,
            DataType.WEB_PAGE: WebPageLoader,
            DataType.QNA_PAIR: LocalQnaPairLoader,
            DataType.TEXT: LocalTextLoader,
            DataType.DOCX: DocxFileLoader,
            DataType.SITEMAP: SitemapLoader,
            DataType.DOCS_SITE: DocsSiteLoader,
        }
        lazy_loaders = {DataType.NOTION}
        if data_type in loaders:
            loader_class = loaders[data_type]
            loader = loader_class()
            return loader
        elif data_type in lazy_loaders:
            if data_type == DataType.NOTION:
                from albertai.loaders.notion import NotionLoader

                return NotionLoader()
            else:
                raise ValueError(f"Unsupported data type: {data_type}")
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

    def _get_chunker(self, data_type: DataType, config):
        """
        Returns the appropriate chunker for the given data type.

        :param data_type: The type of the data to chunk.
        :return: The chunker for the given data type.
        :raises ValueError: If an unsupported data type is provided.
        """
        chunker_classes = {
            DataType.YOUTUBE_VIDEO: YoutubeVideoChunker,
            DataType.PDF_FILE: PdfFileChunker,
            DataType.WEB_PAGE: WebPageChunker,
            DataType.QNA_PAIR: QnaPairChunker,
            DataType.TEXT: TextChunker,
            DataType.DOCX: DocxFileChunker,
            DataType.WEB_PAGE: WebPageChunker,
            DataType.DOCS_SITE: DocsSiteChunker,
            DataType.NOTION: NotionChunker,
        }
        if data_type in chunker_classes:
            chunker_class = chunker_classes[data_type]
            chunker = chunker_class(config)
            chunker.set_data_type(data_type)
            return chunker
        else:
            raise ValueError(f"Unsupported data type: {data_type}")
