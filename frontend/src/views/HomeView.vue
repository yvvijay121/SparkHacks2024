<script setup>
import { userAccountStore } from '../stores/userAccountStore';
import { ref, onMounted } from 'vue';

const usersStore = userAccountStore();
const log = ref([]);
const drugs = ref([]);

onMounted(() => {
  if (usersStore.username != null) {
    fetch("http://127.0.0.1:5000/get_logs/" + usersStore.username)
      .then(response => response.json())
      .then(data => {
        log.value = date_sorted(data.logs.filter(entry => new Date(entry.end_time) >= new Date()));
      });
    fetch("http://127.0.0.1:5000/get_drugs/" + usersStore.username)
      .then(response => response.json())
      .then(data => {
        drugs.value = data.drugs;
      });
  }
});

function searchValueInList(list, id) {
  for (let i = 0; i < list.length; i++) {
    if (list[i].unii == id) {
      return list[i];
    }
  }
}

function date_sorted(logs) {
  return logs.sort((a, b) => {
    return new Date(a.end_time) - new Date(b.end_time);
  });
}
</script>

<template>
  <div class="notification is-danger" v-if="usersStore.username == null">
    Please select a username first to continue!
  </div>
  <div class="container" v-else>
    <h1 class="title is-3">Upcoming Medications</h1>
    <div class="card m-2" v-for="(log, index) in log" :key="index">
      <div class="card-content container has-text-centered">
        <p class="title level-item is-4">{{ searchValueInList(drugs, log.drug_id).generic_name }}</p>
        <p class="title level-item is-6">{{ searchValueInList(drugs, log.drug_id).dosage }} mg</p>
        <br>
        <p class="subtitle is-italic is-6"><strong>Take between:</strong> {{ log.start_time }} - {{ log.end_time }}</p>
        <ul class="content">
          <li>{{ searchValueInList(drugs, log.drug_id).instructions }}</li>
        </ul>
        <div class="field">
          <label class="checkbox">
            <input type="checkbox" disabled checked v-model="log.taken">
            Taken yet
          </label>
        </div>
      </div>
    </div>
  </div>
</template>
