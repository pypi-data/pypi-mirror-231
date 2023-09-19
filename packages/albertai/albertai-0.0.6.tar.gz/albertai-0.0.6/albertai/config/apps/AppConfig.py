import os
from typing import Optional

try:
    from chromadb.utils import embedding_functions
except RuntimeError:
    from embedchain.utils import use_pysqlite3

    use_pysqlite3()
    from chromadb.utils import embedding_functions

from .BaseAppConfig import BaseAppConfig


class AppConfig(BaseAppConfig):
    """
    Config to initialize an embedchain custom `App` instance, with extra config options.
    """

    def __init__(
        self,
        log_level=None,
        host=None,
        port=None,
        id=None,
        collection_name=None,
        collect_metrics: Optional[bool] = None,
    ):
        """
        :param log_level: Optional. (String) Debug level
        ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'].
        :param host: Optional. Hostname for the database server.
        :param port: Optional. Port for the database server.
        :param id: Optional. ID of the app. Document metadata will have this id.
        :param collection_name: Optional. Collection name for the database.
        :param collect_metrics: Defaults to True. Send anonymous telemetry to improve embedchain.
        """
        super().__init__(
            log_level=log_level,
            embedding_fn=AppConfig.default_embedding_function(),
            host=host,
            port=port,
            id=id,
            collection_name=collection_name,
            collect_metrics=collect_metrics,
        )

    @staticmethod
    def default_embedding_function():
        """
        Sets embedding function to default (`text-embedding-ada-002`).

        :raises ValueError: If the template is not valid as template should contain
        $context and $query
        :returns: The default embedding function for the app class.
        """
        if os.getenv("OPENAI_API_KEY") is None and os.getenv("OPENAI_ORGANIZATION") is None:
            raise ValueError("OPENAI_API_KEY or OPENAI_ORGANIZATION environment variables not provided")  # noqa:E501
        return embedding_functions.OpenAIEmbeddingFunction(
            api_key=os.getenv("OPENAI_API_KEY"),
            organization_id=os.getenv("OPENAI_ORGANIZATION"),
            model_name="text-embedding-ada-002",
        )
