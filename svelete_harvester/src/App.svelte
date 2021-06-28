<script>

import { scholar, foodpath, runit } from './functions.js';
</script>

<main>
	<div style="width: 80%; display: inline-block;">
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
		<button style="font-family: Arial; width: 150px; height: 50px; border-radius: 5px;" id="scholar" on:click={() => scholar(document.getElementById("question").value)}>Search</button>
		
		
	</div>
	<h3>Try This</h3>
    <form>
        <textarea id="yourcode" cols="40" rows="10">import turtle

t = turtle.Turtle()
t.forward(100)

print "Hello World" 
</textarea><br />
        <button type="button" on:click={()=>runit(document.getElementById("yourcode").value, document.getElementById("output"))}>Run</button>
    </form>
    <pre id="output"></pre>
	<div class="show-data" style="width: 90%;"></div>	
</main>

<style>
</style>