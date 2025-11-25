from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.post import PostCreate

async def get_posts_from_db(db: AsyncSession) -> list[dict]:
    return [
        {"id": 1, "title": "First Post", "content": "This is the 1st post.", "Owner_id": 1},
        {"id": 2, "title": "First Post", "content": "This is the 2nd post.", "Owner_id": 2},
    ]

async def create_post(
        db: AsyncSession,
        data: PostCreate,
        owner_id: int
):
    title = data.title
    content = data.content
    user_id = owner_id
    
    return True