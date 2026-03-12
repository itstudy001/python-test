from utils import get_movie_info

def test_get_movie_info():
    test_url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=185293"
    title, image, desc = get_movie_info(test_url)
    print(title)
    print(image)
    print(desc)
    assert title == "내일의 기억 : 네이버 검색"
    assert image == "https://search.pstatic.net/common?type=o&size=176x264&quality=85&direct=true&src=https%3A%2F%2Fs.pstatic.net%2Fmovie.phinf%2F20210406_131%2F1617688160755B157W_JPEG%2Fmovie_image.jpg%3Ftype%3Dw640_2"
    assert desc == """사고로 기억을 잃은 채 깨어난 수진 옆엔 자상한 남편 지훈이 그녀를 세심하게 돌봐주고 있다. 그리고 집에 돌아온 후, 마주친 이웃들의 위험한 미래가 보이기 시작하자 수진은 혼란에 빠진다. 그러던 어느 날 길에서 만난 옛 직장 동료는 수진을 걱정하며 지훈에 대한 믿기 힘든 소리를 하고, 때마침 발견한 사진에서 사진 속 남편 자리엔 지훈이 아닌 다른 남자가 있다. 설상가상 수진은 알 수 없는 남자가 자신을 위협하는 환영에 시달리는데……"""
