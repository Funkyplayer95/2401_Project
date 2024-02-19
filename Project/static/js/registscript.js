
const form = document.querySelector('form');
const input_id = document.querySelector('input[name=userid]');
const input_pw = document.querySelector('input[name=password]');
const input_re_pw = document.querySelector('input[name=re_password]');

const id_error = document.querySelector('.id_error');
const pw_error = document.querySelector('.pw_error');
const re_pw_error = document.querySelector('.re_pw_error');

const joomin1Input = document.querySelector('input[name=joomin1]');
const joomin2Input = document.querySelector('input[name=joomin2]');
const joomin_error = document.querySelector('.joomin_error');



//Email 인증 전송
function sendEmail() {
    //밖에 const를 뺏으나 인식이 안되어서 function안으로 넣음.
    const email1 = document.getElementById('emailId').value; //아이디 부분
    const email2 = document.getElementById('domain-txt').value; // 도메인 부분
    const email = email1 + "@" + email2; // full Email
    const xhr = new XMLHttpRequest(); // 서버로 보낼 객체 생성
    xhr.open('POST', '/send_code_email/', true); // post방식으로 해당 이름으로, 비동기 여부
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); // 서버데이터를 url인코딩 방식으로 보낸다.
    xhr.onreadystatechange = function () { // 상태에 따라 바꾸는 이벤트 핸들러
        if (xhr.readyState === 4 && xhr.status === 200) { // 현재 요청상태가 완료되었거나(4), 성공적으로 작업을 완료할경우(200)
            const response = JSON.parse(xhr.responseText); //responseText는 서버로받은 데이터. json.parse = js데이터로 변환
            if (response.status === 'success') { // 성공일경우
                alert('이메일로 인증 코드를 보냈습니다.'); // true code
            } else {alert('이메일 코드 전송을 실패했습니다.' + response.message);} //실패일경우 false code : 실패여부 메세지 출력.
        }}
    const data = `email=${email}`; //data로 보낼건데, 'email'로 설정한것은 const email랑 동일시 하다는 코드.
    xhr.send(data); //data를 보낸다.
}
// 인증번호 확인 코드
function verifyCode() {
    const code = document.getElementById('code').value; // 메일로 받은 인증코드 입력창
    const email1 = document.getElementById('emailId').value; // 아이디 부분
    const email2 = document.getElementById('domain-txt').value; // 도메인 부분
    const email = email1 + "@" + email2; // full email
    const xhr = new XMLHttpRequest(); // 서버로 보낼 객체 생성
    xhr.open('POST', '/verify_code/', true); // post방식으로 해당 이름으로, 비동기 여부
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); // 서버데이터를 url인코딩 방식으로 보낸다.
    xhr.onreadystatechange = function () { // 상태에 따라 바꾸는 이벤트 핸들러
        if (xhr.readyState === 4 && xhr.status === 200) { // 현재 요청상태가 완료되었거나(4), 성공적으로 작업을 완료할경우(200)
            const response = JSON.parse(xhr.responseText); //responseText는 서버로받은 데이터. json.parse = js데이터로 변환
            if (response.status === 'success') { // 성공일 경우
                alert('인증이 성공되었습니다.'); // true code
            } else {alert('인증에 실패하였습니다. : ' + response.message);} //실패일 경우 false code : 실패여부 메시지 출력.
        }}
    const data = `email=${email}&code=${code}`; // email과 code를 보낼 준비를 한다.
    xhr.send(data); // email / code를 서버로 보낸다.
}


//주민등록번호 앞부분 코드. 숫자만 입력되도록 / 월이 13월이 넘지않도록.
function inputNum1(id) {
    var element = document.getElementById('joomin1');
    element.value = element.value.replace(/[^0-9]/gi, ""); // 대괄호 안 [^] =부정, 0-9 = 숫자, /gi = 전역에 대소문자구분없이 검색 >> 숫자가아니면 ""로 바꾼다.
    
    var inputMonth = parseInt(id.substr(2, 2)); // 입력된 주민등록번호의 세번째와 네번째 자리 (월) substr(자를 문자열의 시작위치, 자를 길이)
    if (inputMonth > 12) { //13월 이상으로 작성 될 경우
        alert("입력이 잘못되었습니다.")
        element.value = ''; //작성된 값을 초기화 시키기.
        return false;
    }
    return true
}

//주민등록번호 뒷부분 코드
function inputNum2(id) {
    var element = document.getElementById('joomin2');
    element.value = element.value.replace(/[^0-9]/gi, ""); // 대괄호 안 [^] =부정, 0-9 = 숫자, /gi = 전역에 대소문자구분없이 검색 >> 숫자가아니면 ""로 바꾼다.
}


// 핸드폰 번호 오로지 숫자만 입력하도록
function inputNum3(id) {
    var element = document.getElementById(id);
    element.value = element.value.replace(/[^0-9]/gi, ""); // 대괄호 안 [^] =부정, 0-9 = 숫자, /gi = 전역에 대소문자구분없이 검색 >> 숫자가아니면 ""로 바꾼다.
}



////////////////////////////////////////////////////////////////////////////////////////////////
// document.getElementById('joomin2').onblur = function () {
//     alert("이래도 가능");
// }  이코드는 onblur를 사용할 수 있는 코드이다.

// onblur 코드 모음.
// 작성하다가 포커스가 벗어날 경우 바로 에러창이 나올 수 있게 진행.
function joomin2_Blur() { // 주민 뒷자리

    const joomin1Value = parseInt(document.getElementById('joomin1').value);
    const joomin2Value = parseInt(document.getElementById('joomin2').value);
    const radioValue = document.querySelector('input[name="gender"]:checked').value;
    if (joomin1Value >= 400000) {
        if ((joomin2Value !== 1 && radioValue === 'M') || (joomin2Value !== 2 && radioValue === 'W')) {
            joomin_error.style.display = 'block'
            return;
        }
        else { joomin_error.style.display = 'none' }
    }
    else if (joomin1Value < 400000) {
        if ((joomin2Value !== 3 && radioValue === 'M') || (joomin2Value !== 4 && radioValue === 'W')) {
            joomin_error.style.display = 'block'
            return;
        }
        else { joomin_error.style.display = 'none' }
    }
}

function id_Blur() { // id값
    const idValue = input_id.value;
    if (idValue.length < 6 || idValue.length > 10) { // 6~10자리가 아닐경우 error표시
        id_error.style.display = 'block';
        return;
    } else { id_error.style.display = 'none'; }
}

function pw_Blur() { // password 값
    const passwordValue = input_pw.value;
    const have_english_specialChar = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-])/.test(passwordValue); // 영어 숫자 특수문자 포함
    // 밑에 설명 추가로 있음.

    if (passwordValue.length < 8 || !have_english_specialChar) { //8자리 미만이거나, 영어 숫자 특수문자가 포함안될경우 error표시
        pw_error.style.display = 'block';
        return;
    } else { pw_error.style.display = 'none'; }
}

function re_pw_Blur() { // 비밀번호 확인 값
    const passwordValue = input_pw.value;
    const re_passwordValue = input_re_pw.value;
    if (re_passwordValue !== passwordValue) {
        re_pw_error.style.display = 'block';
        return;
    } else { re_pw_error.style.display = 'none'; }
}
////////////////////////////////////////////////////////////////////////////////////////////////

// 아이디 입력창에 한글 입력 안되도록 설정하는 코드
function english_number_id() {
    var elementId = document.getElementById('id');
    elementId.value = elementId.value.replace(/[^a-zA-Z0-9]/g, ""); // a-z 소문자 모두, A-Z 대문자 모두, 0-9 숫자 모두, g = 전역검색, i= ingore case = 대소문자 구분x 전체
    // 영어 소문자, 대문자, 숫자가 아닌 문자를 찾아 ''로 만든다 
}

// 이메일 부분 참고 코드
const domainListEl = document.getElementById('domain-list')
const domainInputEl = document.getElementById('domain-txt')
// select 옵션 변경 시
domainListEl.addEventListener('change', (event) => {
    // option에 있는 도메인 선택 시
    if (event.target.value !== "type") { // 직접입력으로 선택하지 않았을 경우
        domainInputEl.value = event.target.value // list의 값을 txt값으로 전환.
        document.getElementById('domain-txt').readOnly = true; // 선택한 값을 수정하지 못하도록 readOnly로 변경
        // disable은 불가. disable submit으로 진행시 값이 안넘어간다고 함. 그래서 readonly로 진행.
    
    } else { // 직접 입력 시
        // input 내용 초기화 & 입력 가능하도록 변경
        document.getElementById('domain-txt').readOnly = false; // 다른도메인 선택시 readOnly가 남아있기에 직접입력선택하면 무조건 해제되도록.
        domainInputEl.value = "" //해당 txt안의 값을 초기화 한다.
    }
})

window.onload = function () { // window가 load되어 있는 동안.
    form.addEventListener('submit', function (event) { // form안에서 submit을 했을 시 추가 이벤트 생성.
        const idValue = input_id.value; // id 값
        
        const passwordValue = input_pw.value; // password 값
        const re_passwordValue = input_re_pw.value; // 비밀번호 확인 값

        const have_english_specialChar = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-])/.test(passwordValue);
        // ^ = 문자열의 시작, (?=.*[a-zA-Z]) = 대소문자가 있는지 확인, (?=.*\d) 숫자가 있는지 확인,
        // (?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]) 특수문자가 있는지 확인. *[] = 0개이상의 문자 뒤에 조건에 있는 패턴이 있는지

        // 아이디 검사 코드
        if (idValue.length < 6 || idValue.length > 10) { // 6~10자리가 아닐경우
            id_error.style.display = 'block'; //hidden 상태의 문구를 block로
            alert('아이디는 6~10자리여야 합니다.');
            event.preventDefault(); // 서버에 데이터를 보내는것을 막아 넘어가지 못하게 한다.
            return;
        } else {
            id_error.style.display = 'none'; // 정상적인 경우 보이지 않게 유지.
        }

        // 비밀번호 검사 코드
        if (passwordValue.length < 8 || !have_english_specialChar) { //8자리 미만이거나, 영어 숫자 특수문자중 하나라도 포함안될경우
            pw_error.style.display = 'block'; //hidden 상태의 문구를 block로
            alert('비밀번호는 8자 이상이며, 영어, 특수문자, 숫자를 모두 포함해야 합니다.');
            event.preventDefault(); // 서버로 데이터 넘어가는것을 막아 방지한다.
            return;
        } else {
            pw_error.style.display = 'none'; // 정상적인 경우 보이지 않게 유지.
        }

        // 비밀번호 확인 검사 코드
        if (re_passwordValue !== passwordValue) { // 비밀번호와 비밀번호 확인값이 동일하지 않는다면
            re_pw_error.style.display = 'block'; //hidden 상태의 문구를 block로
            alert('비밀번호와 일치하지 않습니다.');
            event.preventDefault(); // 서버로 데이터 넘어가는것을 막아 방지한다.
            return;
        } else {
            re_pw_error.style.display = 'none'; // 정상적인 경우 보이지 않게 유지.
        }

        //주민등록번호 검사 코드
        const joomin1Value = parseInt(joomin1Input.value); // 앞부분의 값을 int로 변환
        const joomin2Value = parseInt(joomin2Input.value); // 뒷부분의 값을 int로 변환
        const radioValue = document.querySelector('input[name="gender"]:checked').value; //radio에서 check되어있는 값을 불러오기.
        if (joomin1Value >= 400000) { // 40년생 이상이면 (40년생 = 80세 이상이기에 그 이상은 불가할거라 생각하여 기준으로 잡음)
            // 00년생 아래 기준
            // 남자를 선택하고 1이 아니거나, 여자를 선택하고 2가 아니면
            if ((joomin2Value !== 1 && radioValue === 'M') || (joomin2Value !== 2 && radioValue === 'W')) {
                joomin_error.style.display = 'block' //hidden 상태의 문구를 block로
                alert('주민등록번호와 성별이 일치하지 않습니다.')
                event.preventDefault(); //데이터 전송 방지.
                return;
            }
            else {
                joomin_error.style.display = 'none' // 정상적인 경우 보이지 않게 유지.
            }
        }
        else if (joomin1Value < 400000) { // 40년생 미만이면 (40년생 = 80세 이상이기에 그 이상은 불가할거라 생각하여 기준으로 잡음)
            // 00년생 이상 기준
            // 남자를 선택하고 3이 아니거나, 여자를 선택하고 4가 아니면
            if ((joomin2Value !== 3 && radioValue === 'M') || (joomin2Value !== 4 && radioValue === 'W')) {
                joomin_error.style.display = 'block' //hidden 상태의 문구를 block로
                alert('주민등록번호와 성별이 일치하지 않습니다.')
                event.preventDefault(); // 데이터 전송 방지.
                return;
            }
            else {
                joomin_error.style.display = 'none' // 정상적인 경우 보이지 않게 유지
            }
        }
    })
};
