
// 주민등록번호 input type=text에 숫자가 아니면 입력이 안되도록 하는 코드
function inputNum1(id) {
    var element = document.getElementById('jumin1');
    element.value = element.value.replace(/[^0-9]/gi, "");
}
function inputNum2(id) {
    var element = document.getElementById('jumin2');
    element.value = element.value.replace(/[^0-9]/gi, "");
}

// 이메일 부분 참고 코드
const domainListEl = document.querySelector('#domain-list')
const domainInputEl = document.querySelector('#domain-txt')
// select 옵션 변경 시
domainListEl.addEventListener('change', (event) => {
  // option에 있는 도메인 선택 시
  if(event.target.value !== "type") {
    // 선택한 도메인을 input에 입력하고 disabled
    domainInputEl.value = event.target.value
    domainInputEl.disabled = true
  } else { // 직접 입력 시
    // input 내용 초기화 & 입력 가능하도록 변경
    domainInputEl.value = ""
    domainInputEl.disabled = false
  }
})



window.onload = function () {
    const form = document.querySelector('form');
    const input_id = document.querySelector('input[name=userid]');
    const input_pw = document.querySelector('input[name=password]');
    const input_re_pw = document.querySelector('input[name=re_password]');

    const id_error = document.querySelector('.id_error');
    const pw_error = document.querySelector('.pw_error');
    const re_pw_error = document.querySelector('.re_pw_error');

    const jumin1Input = document.querySelector('input[name=jumin1]');
    const jumin2Input = document.querySelector('input[name=jumin2]');
    const jumin_error = document.querySelector('.jumin_error')
    // console.log(input_id, input_pw, input_re_pw, id_error, pw_error, re_pw_error,jumin1Input,jumin2Input,jumin_error);



    form.addEventListener('submit', function (event) {
        // 아이디 검사 코드
        const idValue = input_id.value;
        if (idValue.length < 6 || idValue.length > 10) { // 6~10자리가 아닐경우 error표시
            id_error.style.display = 'block';
            alert('아이디는 6~10자리여야 합니다.');
            event.preventDefault();
            return;
        } else {
            id_error.style.display = 'none';
        }
        
    

        // 비밀번호 검사 코드
        const passwordValue = input_pw.value;
        const have_english_specialChar = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-])/.test(passwordValue); // 영어 숫자 특수문자 포함
        if (passwordValue.length < 8 || !have_english_specialChar) { //8자리 미만이거나, 영어 숫자 특수문자가 포함안될경우 error표시
            pw_error.style.display = 'block';
            alert('비밀번호는 8자 이상이며, 영어, 특수문자, 숫자를 모두 포함해야 합니다.');
            event.preventDefault();
            return;
        } else {
            pw_error.style.display = 'none';
        }

        // 비밀번호 확인 검사 코드
        const re_passwordValue = input_re_pw.value;
        if (re_passwordValue !== passwordValue) {
            re_pw_error.style.display = 'block';
            alert('비밀번호와 일치하지 않습니다.');
            event.preventDefault();
            return;
        } else {
            re_pw_error.style.display = 'none';
        }

        //주민등록번호 검사 코드

        const jumin1Value = parseInt(jumin1Input.value);
        const jumin2Value = parseInt(jumin2Input.value);
        const radioValue = document.querySelector('input[name="gender"]:checked').value;
        if (jumin1Value >= 400000){
            if ((jumin2Value !== 1 && radioValue === 'M') || (jumin2Value !== 2 && radioValue === 'W')){
                jumin_error.style.display = 'block'
                alert('주민등록번호와 성별이 일치하지 않습니다.')
                event.preventDefault();
                return;
            }
            else {
                jumin_error.style.display = 'none'
            }
        }
        else if (jumin1Value < 400000){
            if ((jumin2Value !== 3 && radioValue === 'M') || (jumin2Value !== 4 && radioValue === 'W')){
                jumin_error.style.display = 'block'
                alert('주민등록번호와 성별이 일치하지 않습니다.')
                event.preventDefault();
                return;
                }
            else {
                jumin_error.style.display = 'none'
            }
        }
    })};
