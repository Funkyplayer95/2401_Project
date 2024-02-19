
const form = document.querySelector('form');
const input_pw = document.querySelector('input[name=newPw]');
const input_re_pw = document.querySelector('input[name=re_newPw]');

const pw_error = document.querySelector('.pw_error');
const re_pw_error = document.querySelector('.re_pw_error');

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

window.onload = function () { // window가 load되어 있는 동안.
    form.addEventListener('submit', function (event) { // form안에서 submit을 했을 시 추가 이벤트 생성.
        const passwordValue = input_pw.value; // password 값
        const re_passwordValue = input_re_pw.value; // 비밀번호 확인 값

        const have_english_specialChar = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-])/.test(passwordValue);
        // ^ = 문자열의 시작, (?=.*[a-zA-Z]) = 대소문자가 있는지 확인, (?=.*\d) 숫자가 있는지 확인,
        // (?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]) 특수문자가 있는지 확인. *[] = 0개이상의 문자 뒤에 조건에 있는 패턴이 있는지

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

    }
    );
}
