const questions = [
	{
			question: "������� ����� 2 � ����?",
			options: ["4", "8", "16", "32"],
			answer: "8"
	},
	{
			question: "��� ����� �� ��������� �����?",
			options: ["apple", "melon", "pear", "squash"],
			answer: "pear"
	},
	{
			question: "������� ���� ����������?",
			options: ["1", "2", "3", "4"],
			answer: "4"
	},
	{
			question: "���������� ������ �� 9?",
			options: ["0", "1", "2", "3"],
			answer: "3"
	},
	{
			question: "������� ������� �� �����?",
			options: ["2", "4", "5", "7"],
			answer: "5"
	}
];

let question_number = 0;
let correct = 0;

document.addEventListener("DOMContentLoaded", () => {
	load_question();
});

function load_question() {
	document.querySelector("#question").innerHTML = questions[question_number].question;
	const options = document.querySelector("#options");
	options.innerHTML = "";
	for (const option of questions[question_number].options) {
		options.innerHTML += `<button class="option">${option}</button>`;
		console.log(option);
	}
	
	document.querySelectorAll(".option").forEach(option => {
		option.onclick = () => {
				if (option.textContent == questions[question_number-1].answer) {
					correct++;
				}
				document.querySelector("#correct").innerHTML = correct + ' of ' + question_number;
				if (question_number <= 4) {
					load_question();
				} else {
					document.querySelector("#question").innerHTML = '�������� ��������';
					document.querySelector("#options").innerHTML = '<a href=quiz.html>��������� ��������</a><br><br>';
					
				}
		}
	});
	
	question_number++;
}