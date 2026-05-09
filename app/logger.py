from datetime import datetime
from .database import log_collection


async def log_action(action: str):

    await log_collection.insert_one({
        "action": action,
        "timestamp": datetime.utcnow()
    })