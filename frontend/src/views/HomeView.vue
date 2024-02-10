<script setup>
import { userAccountStore } from '../stores/userAccountStore';
import { ref, onMounted } from 'vue';

const usersStore = userAccountStore();
const log = ref([]);

onMounted(() => {
  if (usersStore.username != null) {
    fetch("http://127.0.0.1:5000/get_logs/" + usersStore.username)
        .then(response => response.json())
        .then(data => {
            log.value = data;
        });
  }
});
</script>

<template>
  <div class="notification is-danger" v-if="usersStore.username == null">
    Please select a username first to continue!
  </div>
  <div class="card" v-else>
    {{  log }}
  </div>
</template>
