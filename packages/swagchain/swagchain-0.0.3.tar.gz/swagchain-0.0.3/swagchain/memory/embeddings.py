from typing import List

import openai

from .vector import *


class Memory(VectorClient):
    """OpenAI Embeddings Client"""
    @property
    def builder(self):
        return QueryBuilder()
       
    async def encode(
        self, texts: List[str], namespace: str
    ) -> List[Embedding]:
        response = await openai.Embedding.acreate(  # type: ignore
            input=texts, model="text-embedding-ada-002"
        )
        response = await openai.Embedding.acreate(
            model="text-embedding-ada-002",
            input=texts,
        )
        data = response["data"]
        return [
            Embedding(
                values=embedding["embedding"],
                metadata={"namespace": namespace, "text": text},
            )
            for embedding, text in zip(data, texts)
        ]

    async def save(self, embeddings: List[Embedding]):
        response = await self.upsert(embeddings=embeddings)
        return response.upsertedCount

    async def search(
        self, text: str, namespace: str, top_k: int
    ) -> List[str]:
        
        embeddings = await self.encode(texts=[text], namespace=namespace)
        expr = (self.builder("namespace") == namespace) & (self.builder("text") != text)
        response = await self.query(
            expr=expr.query,
            vector=embeddings[0].values,
            topK=top_k,
        )
        return [match.metadata["text"] for match in response.matches]  # type: ignore
