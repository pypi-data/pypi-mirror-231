from typing import Optional

from langchain.text_splitter import RecursiveCharacterTextSplitter

from albertai.chunkers.base_chunker import BaseChunker
from albertai.config.AddConfig import ChunkerConfig


class WebPageChunker(BaseChunker):
    """Chunker for web page."""

    def __init__(self, config: Optional[ChunkerConfig] = None):
        if config is None:
            config = ChunkerConfig(chunk_size=500, chunk_overlap=0, length_function=len)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            length_function=config.length_function,
        )
        super().__init__(text_splitter)
