<script>
  let name = 'world'
  let names = ['Sam', 'John', 'Mary', 'Pete']

  function generateName() {
      name = names[Math.floor(Math.random() * names.length)]
  }
</script>

<style>
  p {
      color: purple;
  }
</style>
<p>Hello {name}!</p>
<button on:click={generateName}>Generate name</button>