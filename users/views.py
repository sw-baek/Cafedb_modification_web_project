from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password


def loginpage(request):
    return render(request, 'users/loginpage.html')


def signup(request):
    return render(request, 'users/signup.html')


def signup_process(request):
    #form 태그 안에 것이 들어온다.
    user_id = request.POST['username']
    user_email = request.POST['email']
    user_password = request.POST['password']
    re_password = request.POST['re_password']
    # tel = request.POST['tel']

    # 원래 있는 아이디면 안된다!
    user_list = User.objects.all()
    if user_list.filter(username=user_id).exists():
        return render(request, 'users/signup.html',
                      {'err_msg': '이미 있는 ID 입니다.'})

    # 비밀번호 같다 => 회원가입가능!!
    elif user_password == re_password:
        User.objects.create_user(username=user_id, password=user_password, email=user_email)
        return redirect('home')

    elif user_password != re_password: #비밀번호가 다를 때
        return render(request, 'users/signup.html',
                      {'err_msg': '비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'users/signup.html',
                      {'err_msg': '내용을 모두 입력하세요.'})


def login_process(request):
    # 클라이언트로부터 POST방식으로 id, pw가 넘어와요!
    u_id = request.POST['username']
    u_pw = request.POST['password']

    #만약 db에 있으면 로그인 시켜주고
    user = auth.authenticate(request,
                             username=u_id,
                             password=u_pw)
    if user is not None :
        #로그인 했다는 사인을 줘야한다!
        user_dict = {'u_id': user.id,
                     'u_name': user.username}
        #session처리
        request.session['loginObj'] = user_dict

        return redirect('home')

    else:
        return render(request, 'users/loginpage.html',
                      {'err_msg': '로그인 실패! 다시 입력하세요.'})


def logout(request):
    auth.logout(request)
    return redirect('home')


def findpassword(request):
    return render(request, 'users/findpassword.html')


def findid(request):
    return render(request, 'users/findid.html')


def modify(request):
    return render(request, 'users/modify.html')


def modifyprocess(request):
    # form 태그 안에 것이 들어온다.
    user_id = request.POST['username']
    user_email = request.POST['email']
    user_password = request.POST['password']
    re_password = request.POST['re_password']

    # 아이디가 일치할때만 회원 정보 수정 가증
    user_list = User.objects.all()
    if user_list.filter(username=user_id).exists(): #아이디가 일치 할 때
        if user_password != re_password: #비밀번호가 다르면 경고!!
            return render(request, 'users/modify.html', {'err_msg': '비밀번호가 일치하지 않습니다.'})

        else: #회원정보 수정해주기!
            instance = User.objects.get(username=user_id)
            instance.set_password(user_password)
            instance.email = user_email
            instance.save()
            return render(request, 'users/loginpage.html', {'suc_msg': '회원정보를 수정하였습니다.'})

    # 아이디가 일치 하지 않는 경우
    else:
        return render(request, 'users/modify.html', {'err_msg': '아이디를 정확히 입력하세요.'})


def withdrawl(request):
    return render(request, 'users/withdrawl.html')


def withdrawlprocess(request):
    # form 태그 안에 것이 들어온다.
    user_id = request.POST['username']
    user_password = request.POST['password']

    user_list = User.objects.all()
    if user_list.filter(username=user_id).exists():  # 아이디가 일치 할 때
        instance = User.objects.get(username=user_id)
        if check_password(instance.password, user_password):
            return render(request, 'users/withdrawl.html', {'err_msg': '비밀번호를 정확히 입력하세요.'})
        else:
            instance.delete()
            return redirect('home')

    # 아이디가 일치 하지 않는 경우
    else:
        return render(request, 'users/withdrawl.html', {'err_msg': '아이디를 정확히 입력하세요.'})

