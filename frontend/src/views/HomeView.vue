<script setup>
import { userAccountStore } from '../stores/userAccountStore';

const usersStore = userAccountStore();
</script>

<template>
  <div class="notification is-danger" v-if="usersStore.username == null">
    Please select a username first to continue!
  </div>
  <div class="card" v-else>
    <div class="card-content">
      <p class="title">

        {{ usersStore.username == null ? 'Select User' : usersStore.username }}
      </p>
    </div>
    <footer class="card-footer">
      <p class="card-footer-item">
        <span>
          View on <a href="https://twitter.com/codinghorror/status/506010907021828096">Twitter</a>
        </span>
      </p>
      <p class="card-footer-item">
        <span>
          Share on <a href="#">Facebook</a>
        </span>
      </p>
    </footer>
  </div>
</template>
