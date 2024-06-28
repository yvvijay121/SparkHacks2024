<script>
import { ref } from 'vue'
const drug = ref('')

export default {
    data() {
        return {
            drug: '',
            sum: []
        }
    },
    methods: {
        getData() {
            console.log(this.drug)
            const url = 'https://connect.medlineplus.gov/service?mainSearchCriteria.v.cs=2.16.840.1.113883.6.69&mainSearchCriteria.v.c=';
            const urlEnd = '&informationRecipient.languageCode.c=en'
            let resultEnd = url.concat(this.drug, urlEnd)
            fetch(resultEnd, {
                mode: 'no-cors',
            })
                .then(res => res.json())
                .then(data => this.sum = data)
                .catch(err => console.log("Error: ", err))
            }
    }
}  
</script>

<template>
    <h1 class="title is-1">Find your drug information</h1>
    <div class="card-content">
        <form @submit.prevent="getData">
            <input v-model="drug" required placeholder="Enter your NDC">
            <button>Go</button>
        </form>
    </div>
    <div class = "card-content">
        <h2>Here is the summary of the drug:</h2>
        {{ sum }}
    </div>
</template>