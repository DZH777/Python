let x1 = 50;
alert(x1);

function hello() {
	alert('Hi!!!');	
	document.querySelector("h1").innerHTML = "Hello!"
	const headings = document.querySelectorAll("h2");
	for (const heading of headings) {
		heading.innerHTML = "Hello!!!!"
	}
}