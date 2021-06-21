<script>
	let scholar = 'default'

	function getScholar(question){
		fetch('./foodpath/'+question)
			.then(d => d.text())
			.then(d => (scholar = d));
	}
</script>

<main>
	<h1>scholar : {scholar}</h1>
	
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>