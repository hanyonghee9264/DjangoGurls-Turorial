import os

from django.http import HttpResponse


def post_list(request):
    """
    / (Root URL)에 해당하는 view
    :param request:
    :return:
    """
    views_file_path = os.path.abspath(__file__)
    blog_application_path = os.path.dirname(views_file_path)
    app_dir = os.path.dirname(blog_application_path)
    template_path = os.path.join(app_dir, 'templates', 'blog', 'post_list.html')

    # with문 사용
    with open(template_path, 'rt') as f:
        ontent = f.read()

    # 파일객체 직접 사용 후 close
    f = open(template_path, 'rt')
    content = f.read()
    f.close()

    # 파일객체를 변수에 할당하지 않고 사용
    content = open(template_path, 'rt').read()

    # templates/blog/post_list.html파일의 내용을 읽어온 후,
    # 해당 내용을 아래에서 리턴해주는 HttpResponse인스턴스 생성시 인수로 넣어준다
    # os.path.abspath(__file__)     <- 코드가 실행중인 파일의 경로를 나타냄
    # os.path.dirname(<겅로>)        <- 특정 경로의 상위폴더를 나타냄
    # os.path.join(<경로>, <폴더/파일명>)  <- 특정 경로에서 하위폴더 또는 하위 파일을 나타냄
    return HttpResponse()
