<script>
export default{
    name:"post",
    data(){
        return{
            posts: {
                ncd: null,
            }
        }
    },
    methods:{
        reverseMessage: function() {    
        fetch('/getDrugData', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.message)
            })
            .then(response => response.json())
            .then(data => this.message = data)
    }
    }
}
</script>

<template>
    <h1 class="title is-1">Find your drug information</h1>
    <div class="card-content">
        <form @submit="drugData">
            <input class="input" type="text" placeholder="Enter you NCD">
            <button v-on:click="getData">Go</button>
        </form>
    </div>
    <div class = "card-content">
        <h2>Here is the summary of the drug:</h2>
        {{ output }}
    </div>
</template>