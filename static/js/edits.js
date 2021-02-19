
function to_list() {
    // location.herf ='/edit/shoplist'
    location.herf ='home'
}

function delete_shop(geocafe_id) {
    let alarm1 = confirm('정말 폐업설정할까요?')
    if(alarm1) {
        location.herf = '/edit/delete/' + geocafe_id
    }
}

function update_info(geocafe_id){
    if (confirm('본인의 상점만 수정할 수 있습니다!')) {
        window.location.herf = '/edit/update/' + geocafe_id
    }
    else{
        return;
    }
}

function check_login(){
    if (confirm('정보를 수정하려면 로그인하세요. 로그인 하시겠습니까?')){
            window.location.href = '/users/loginpage'
        }
}