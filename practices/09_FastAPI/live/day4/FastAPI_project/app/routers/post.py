from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.post import PostCreate, PostRead



router = APIRouter(prefix="/posts", tags=["posts"])


# GET /posts
@router.get("", response_model=list[PostRead])
async def get_posts(
    db: AsyncSession = Depends(get_db)
):  
    from app.crud.post import get_posts_from_db
    result = await get_posts_from_db(db)
    return result

# GET /posts/{post_id}
@router.get("/{post_id}", response_model=list[PostRead])
async def get_post_by_post_id(post_id: int):
    return {"test": str(post_id) + "get_post_id"}

# POST /posts
@router.post(""
,     status_code=status.HTTP_201_CREATED,
)
async def post_posts(
    payload: PostCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> int:
    from app.crud import post as post_crud
    owner_id = current_user.id
    new_post_id  =post_crud.create_post(db, payload, owner_id)
    return new_post_id

# UPDATE /posts/{post_id}
@router.put("/{post_id}")
async def update_post(post_id: int):
    return {"test": str(post_id) + "updated"}

# DELETE /posts/{post_id}
@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    return {"test": str(post_id) + "deleted"}




# GET /posts/{post_id}/comments
@router.get("/{post_id}/comments")
async def get_comments(post_id: int):
    return {"test": "ok"}

# GET /posts/{post_id}/comments/{comment_id}
@router.get("/{post_id}/comments/{comment_id}")
async def get_comment_by_post_id_and_comment_id(post_id: int, comment_id: int):
    return {"test": "ok"}

# POST /posts/{post_id}/comments
@router.post("/{post_id}/comments")
async def post_comment_by_post_id(post_id: int):
    return {"test": "ok"}

# UPDATE /posts/{post_id}/comments/{comment_id}
@router.put("/{post_id}/comments/{comment_id}")
async def update_comment_by_post_id_and_comment_id(post_id: int, comment_id: int):
    return {"test": "ok"}

# DELETE /posts/{post_id}/comments/{comment_id}
@router.delete("/{post_id}/comments/{comment_id}")
async def delete_comment_by_post_id_and_comment_id(post_id: int, comment_id: int):
    return {"test": "ok"}
