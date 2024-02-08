
const form = document.querySelector('form');
const input_id = document.querySelector('input[name=userid]');
const input_pw = document.querySelector('input[name=password]');
const input_re_pw = document.querySelector('input[name=re_password]');

const id_error = document.querySelector('.id_error');
const pw_error = document.querySelector('.pw_error');
const re_pw_error = document.querySelector('.re_pw_error');

const jumin1Input = document.querySelector('input[name=jumin1]');
const jumin2Input = document.querySelector('input[name=jumin2]');
const jumin_error = document.querySelector('.jumin_error');

const email1 = document.getElementById('emailId').value;
const email2 = document.getElementById('domain-txt').value;
const email = email1 + "@" + email2;

//Email 인증 코드
function sendEmail() {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/send_code_email/', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            if (response.status === 'success') {
                alert('이메일로 인증 코드를 보냈습니다.');
            } else {alert('이메일 코드 전송을 실패했습니다.' + response.message);}
        }
    }
    const data = `email=${email}`; //여기부분 확인해볼것. `email=${email}` 앞부분이 어디를 뜻하는지 알아야함.
    xhr.send(data);
}


//주민등록번호 앞부분 코드
function inputNum1(id) {
    var element = document.getElementById('jumin1');
    element.value = element.value.replace(/[^0-9]/gi, "");
    var inputMonth = parseInt(id.substr(2, 2)); // 입력된 주민등록번호의 세번째와 네번째 자리 (월)
    if (inputMonth > 12) {
        alert("입력이 잘못되었습니다.")
        element.value = '';
        return false;
    }
    return true
}

//주민등록번호 뒷부분 코드
function inputNum2(id) {
    var element = document.getElementById('jumin2');
    element.value = element.value.replace(/[^0-9]/gi, "");
}


// 핸드폰 번호 오로지 숫자만 입력하도록
function inputNum3(id) {
    var element = document.getElementById('phone');
    element.value = element.value.replace(/[^0-9]/gi, "");
}

// document.getElementById('jumin2').onblur = function () {
//     alert("바보");0
// }  이코드는 onblur를 사용할 수 있는 코드이다.

function jumin2_Blur() {

    const jumin1Value = parseInt(document.getElementById('jumin1').value);
    const jumin2Value = parseInt(document.getElementById('jumin2').value);
    const radioValue = document.querySelector('input[name="gender"]:checked').value;
    if (jumin1Value >= 400000) {
        if ((jumin2Value !== 1 && radioValue === 'M') || (jumin2Value !== 2 && radioValue === 'W')) {
            jumin_error.style.display = 'block'
            return;
        }
        else { jumin_error.style.display = 'none' }
    }
    else if (jumin1Value < 400000) {
        if ((jumin2Value !== 3 && radioValue === 'M') || (jumin2Value !== 4 && radioValue === 'W')) {
            jumin_error.style.display = 'block'
            return;
        }
        else { jumin_error.style.display = 'none' }
    }
}

function id_Blur() {
    const idValue = input_id.value;
    if (idValue.length < 6 || idValue.length > 10) { // 6~10자리가 아닐경우 error표시
        id_error.style.display = 'block';
        return;
    } else { id_error.style.display = 'none'; }
}
function english_number_id() {
    var elementId = document.getElementById('id');
    elementId.value = elementId.value.replace(/[^a-zA-Z0-9]/g, ""); // a-z 소문자 모두, A-Z 대문자 모두, 0-9 숫자 모두, g = 전역검색, i= ingore case = 대소문자 구분x 전체
    // 영어 소문자, 대문자, 숫자가 아닌 문자를 찾아 ''로 만든다 
}

function pw_Blur() {
    const passwordValue = input_pw.value;
    const have_english_specialChar = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-])/.test(passwordValue); // 영어 숫자 특수문자 포함
    if (passwordValue.length < 8 || !have_english_specialChar) { //8자리 미만이거나, 영어 숫자 특수문자가 포함안될경우 error표시
        pw_error.style.display = 'block';
        return;
    } else { pw_error.style.display = 'none'; }
}

function re_pw_Blur() {
    const passwordValue = input_pw.value;
    const re_passwordValue = input_re_pw.value;
    if (re_passwordValue !== passwordValue) {
        re_pw_error.style.display = 'block';
        return;
    } else { re_pw_error.style.display = 'none'; }
}

// 이메일 부분 참고 코드
const domainListEl = document.getElementById('domain-list')
const domainInputEl = document.getElementById('domain-txt')
// select 옵션 변경 시
domainListEl.addEventListener('change', (event) => {
    // option에 있는 도메인 선택 시
    if (event.target.value !== "type") {
        // 선택한 도메인을 input에 입력하고 disabled
        domainInputEl.value = event.target.value
        document.getElementById('domain-txt').readOnly = true;
    } else { // 직접 입력 시
        // input 내용 초기화 & 입력 가능하도록 변경
        document.getElementById('domain-txt').readOnly = false;
        domainInputEl.value = ""
        //disabled은 input객체 비활성화 처리가능. form전송시 전송 x
    }
})

window.onload = function () {
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
        if (jumin1Value >= 400000) {
            if ((jumin2Value !== 1 && radioValue === 'M') || (jumin2Value !== 2 && radioValue === 'W')) {
                jumin_error.style.display = 'block'
                alert('주민등록번호와 성별이 일치하지 않습니다.')
                event.preventDefault();
                return;
            }
            else {
                jumin_error.style.display = 'none'
            }
        }
        else if (jumin1Value < 400000) {
            if ((jumin2Value !== 3 && radioValue === 'M') || (jumin2Value !== 4 && radioValue === 'W')) {
                jumin_error.style.display = 'block'
                alert('주민등록번호와 성별이 일치하지 않습니다.')
                event.preventDefault();
                return;
            }
            else {
                jumin_error.style.display = 'none'
            }
        }
    })
};
