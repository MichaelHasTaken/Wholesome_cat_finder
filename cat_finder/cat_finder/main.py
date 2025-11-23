
import requests
import webbrowser

# The Cat API의 무작위 이미지 엔드포인트
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

def get_random_cat_url():
    """
    무작위 고양이 이미지의 URL을 가져와 반환합니다.
    """
    try:
        # API에 요청을 보냅니다. (JSON 응답을 기대합니다)
        response = requests.get(CAT_API_URL)
        response.raise_for_status() # HTTP 오류가 발생하면 예외를 발생시킵니다.
        
        # 응답은 보통 JSON 리스트 형태이며, 첫 번째 항목에서 'url' 키를 추출합니다.
        data = response.json()
        if data and 'url' in data[0]:
            cat_url = data[0]['url']
            return cat_url
        else:
            return "API 응답에서 유효한 URL을 찾을 수 없습니다."

    except requests.exceptions.RequestException as e:
        return f"API 호출 중 오류가 발생했습니다: {e}"

def show_random_cat():
    """
    무작위 고양이 이미지를 사용자의 기본 웹 브라우저로 띄워줍니다.
    """
    cat_url = get_random_cat_url()
    
    if cat_url.startswith("http"):
        print(f"고양이 URL: {cat_url}")
        webbrowser.open(cat_url)
    else:
        print(f"오류: {cat_url}")