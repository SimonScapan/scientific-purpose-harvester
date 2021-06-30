<script>
import { scholar, foodpath } from './functions.js';
function spinner() {document.getElementsByClassName("loader")[0].style.display = "block";}
</script>

<main style="text-align: center;">
<div style="width: 80%; display: inline-block; text-align: center;">
	<h1 style="font-family: Arial; color: blue;">Welcome to SPH - Scientific Purpose Harvester</h1>
	<div style="background-color: grey; border-radius: 5px;">
		<br><br>
		<p style="font-family: Arial; color: white">
			With SPH it is possible to search for web pages and scientific papers on the Internet based on a question or a term.
			SPH uses Google scholar to display scientific papers and ranks them based on the frequency of citations in other scientific papers. 
			<br><br>
			After requesting results based on your input it takes a moment until the result is displayed.
		</p>
		<br><br>
	</div>
	<br><br>
	<input style="width: 500px; height: 40px; border-radius: 5px; font-size: 1em" placeholder=" Type your question" type="text" id="question" name="question">
	<br><br>
	<!-- <button style="font-family: Arial; width: 150px; height: 50px; border-radius: 5px;" id="foodpath" on:click={() => foodpath(document.getElementById("question").value)}">Google results</button> -->
	<button style="font-family: Arial; width: 150px; height: 50px; border-radius: 5px;" id="scholar" on:click={() => scholar(document.getElementsByClassName("loader"), document.getElementById("question").value)}>Search</button>
	<div class="loader">
	  <div class="loading">
	  </div>
	</div>
	
	
  	
</div>

<div class="show-data" style="width: 90%;"></div>	
</main>

<style>
</style>