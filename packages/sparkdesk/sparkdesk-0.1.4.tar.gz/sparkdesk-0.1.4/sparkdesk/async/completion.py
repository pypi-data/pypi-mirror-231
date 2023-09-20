import logging
from typing import Any, AsyncIterator, Dict, List

from websockets import connect

from sparkdesk.completion import BaseChatCompletion

logger = logging.getLogger(__name__)


class ChatCompletion(BaseChatCompletion):
    async def create(
        self, message_text: List[Dict[str, str]]
    ) -> AsyncIterator[Dict[str, Any]]:
        """
        Create chat completion.
        reference: https://www.xfyun.cn/doc/spark/Web.html

        Args:
            message_text:
                A list of dictionaries containing the message content.
                The total length of the message content should be less than 8192.
                one token is approximately equal to 1.5 Chinese characters or
                0.8 English words.
                ex: [{"role": "user", "content": "Hi"}]

        Yields:
            An iterator that yields the processed response messages from the websocket.
        """
        async with connect(self.authentication.get_authorization_url()) as websocket:
            input_message = self._build_ws_input_message(message_text)
            logger.debug(f"send: {input_message}")
            await websocket.send(input_message)

            response_message = await websocket.recv()
            logger.debug(f"recv: {response_message}")
            while True:
                processed_ws_response_message = self._process_ws_response_message(
                    response_message
                )
                yield processed_ws_response_message
                # if last message, exit
                if processed_ws_response_message["header"]["status"] == 2:
                    break
                response_message = await websocket.recv()
                logger.debug(f"recv: {response_message}")
