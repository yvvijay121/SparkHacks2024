<script setup>
import { ref, onMounted, watch } from 'vue';
import { userAccountStore } from '../stores/userAccountStore';

const drugs = ref([]);

onMounted(() => {
    if (usersStore.username != null) {
        fetch("http://127.0.0.1:5000/get_drugs/" + usersStore.username)
            .then(response => response.json())
            .then(data => {
                drugs.value = data.drugs;
            });
    }
});

const usersStore = userAccountStore();

</script>
<template>
    <div class="notification is-danger" v-if="usersStore.username == null">
        Please select a username first to continue!
    </div>
    <div class="container box" v-else>
        <h1 class="title is-3">View All Medications</h1>
        <div class="table-container">
            <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>Medication</th>
                    <th>Dosage (mg)</th>
                    <th>Drug Route</th>
                    <th>Start Date</th>
                    <th>End Date</th>
                    <th>Instructions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(drug, index) in drugs">
                    <td>{{ drug.generic_name }}</td>
                    <td>{{ drug.dosage }}</td>
                    <td>{{ drug.drug_route }}</td>
                    <td>{{ drug.start_date }}</td>
                    <td>{{ drug.end_date }}</td>
                    <td>{{ drug.instructions }}</td>
                </tr>
            </tbody>
        </table>
        </div>
    </div>
</template>

<style>
li {
    list-style-type: none;
}
</style>
