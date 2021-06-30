import $ from "jquery"
// import SK from "http://www.skulpt.org/js/skulpt-stdlib.js"
// import * from "http://www.skulpt.org/js/skulpt.min.js"
// import * from "http://www.skulpt.org/js/skulpt-stdlib.js");


export function foodpath(question) {
$.ajax({
			// url: "http://localhost:5000/foodpath",
			url: "http://85.214.28.167:5000/foodpath",
			type: "POST",
			data: {question:question}

		}).done(function(response) {

			var html= "<br><br><br>";

			response =response.result;
				$.each(response,function(key,val){
				console.log(val);
					html+="<p>"+val+"<p>"
				});
				html +="<br>";
				$(".show-data").html(html);
			});
};

export function scholar(question) {
$.ajax({
			// url: "http://localhost:5000/scholar",
			url: "http://85.214.28.167:5000/foodpath",
			type: "POST",
			data: {question:question}
		}).done(function(response) {
			var html= "<br><br><br>";
			response = response.result;
            console.log(response)
				$.each(response,function(key,val){
				console.log(val);
					html+="<p>"+val+"<p>"
				});
				html +="<br>";
				$(".show-data").html(html);
			});
};

// export function runit(prog, mypre) { 
//     // var prog = document.getElementById("yourcode").value; 
//     // var mypre = document.getElementById("output"); 
//     mypre.innerHTML = ''; 
//     Sk.pre = "output";
//     Sk.configure({output:outf, read:builtinRead}); 
//     (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
//     var myPromise = Sk.misceval.asyncToPromise(function() {
//         return Sk.importMainWithBody("<stdin>", false, prog, true);
//     });
//     myPromise.then(function(mod) {
//         console.log('success');
//     },
//         function(err) {
//         console.log(err.toString());
//     });
//  } 