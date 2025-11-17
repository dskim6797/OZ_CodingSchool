"""
라우트 (Controller Layer)
- 사용자가 요청한 URL을 처리하고
- 서비스 계층을 호출해서 DB 조작
- 결과를 템플릿에 전달
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.review_service import get_all_reviews, get_avg_rating, create_review, get_review_by_id, update_review, delete_review
from app.models import Review # 타입 힌트와 모델 사용을 위해 임포트

# 블루프린트 객체 생성
review_bp = Blueprint('review', __name__)

@review_bp.route('/')
def index():
    """리뷰 목록 + 평균 별점"""
    # 리뷰 목록을 가져오세요 (service의 get_all_reviews)
    reviews = get_all_reviews()

    # 평균 별점을 계산하세요 (리뷰가 있으면 rating 평균, 없으면 0)
    avg_rating = get_avg_rating(reviews)
    # avg_rating = sum(r.rating for r in reviews) / len(reviews) if reviews else 0
            
    # index.html 템플릿에 reviews, avg_rating을 전달해서 렌더링하세요
    return render_template('index.html', reviews=reviews, avg_rating=avg_rating)

@review_bp.route('/new', methods=['GET', 'POST'])
def new_review():
    """새 리뷰 작성"""
    # request.method 가 POST 인지 확인
    if request.method == 'POST':
        try:
            # form 데이터(title, content, rating) 받기
            title = request.form['title']
            content = request.form['content']
            rating = int(request.form['rating'])
            
            if not (1 <= rating <= 5):
                flash("별점은 1에서 5 사이여야 합니다.", 'error')
                return redirect(url_for('review.new_review'))

            # service의 create_review 함수를 호출해서 DB에 저장
            create_review(title=title, content=content, rating=rating)
            flash("새 리뷰가 성공적으로 작성되었습니다.", 'success')
            # index 페이지 redirect
            return redirect(url_for('review.index')) # 저장 후 index 페이지로 redirect
        
        except ValueError:
            flash("별점은 유효한 정수여야 합니다.", 'error')
            return redirect(url_for('review.new_review'))
    
    # GET 요청일 경우 new.html 템플릿을 렌더링
    return render_template('new.html')

@review_bp.route('/edit/<int:review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    """리뷰 수정"""
    # 수정 페이지에서 수정 버튼 눌렀을 때 = POST
    if request.method == 'POST':
        try:
            # 수정된 데이터(title, content, rating)를 받아서 service의 update_review 실행
            title = request.form['title']
            content = request.form['content']
            rating = int(request.form['rating'])
            
            if not (1 <= rating <= 5):
                flash("별점은 1에서 5 사이여야 합니다.", 'error')
                return redirect(url_for('review.edit_review', review_id=review_id))

            update_review(review_id, title, content, rating)
            flash("리뷰가 성공적으로 수정되었습니다.", 'success')
            # 수정 후 index 페이지 redirect
            return redirect(url_for('review.index'))
            
        except ValueError:
            flash("별점은 유효한 정수여야 합니다.", 'error')
            return redirect(url_for('review.edit_review', review_id=review_id))
    
    # 메인페이지에서 수정 버튼 눌렀을 때 = GET
    # service의 get_review_by_id 함수로 해당 id의 리뷰 가져오기
    review = get_review_by_id(review_id)    
    # 기존 리뷰 전달, edit.html 템플릿을 렌더링
    return render_template('edit.html', review=review)

@review_bp.route('/delete/<int:review_id>', methods=['GET', 'POST'])
def delete_review_route(review_id):
    """리뷰 삭제"""
    if request.method == 'GET':
        # service의 delete_review 함수를 실행해서 해당 리뷰를 삭제
        delete_review(review_id)
        flash("리뷰가 성공적으로 삭제되었습니다.", 'success')
        # 삭제 후 index 페이지 redirect
        return redirect(url_for('review.index'))
    return
