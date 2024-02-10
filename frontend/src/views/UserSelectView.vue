<script setup>
import { ref, onMounted, watch } from 'vue';
import { userAccountStore } from '../stores/userAccountStore';

const users = ref([]);

onMounted(() => {
    fetch("http://127.0.0.1:5000/get_users")
        .then(response => response.json())
        .then(data => {
            users.value = data.users;
        });
});

const pick = ref('');

const usersStore = userAccountStore();

watch(pick, (newValue) => {
    usersStore.username = newValue;
});


</script>
<template>
    <div class="box">
        <h1 class="title is-3">Select User</h1>
        <li v-for="(user, index) in users">
            <div class="switch-field m-3">
                <input type="radio" id="radio-one" class="m-2" name="switch-one" v-model="pick" :value="user.user_name" />
                <label for="radio-one"> {{ user.first_name }} {{ user.last_name }} </label>
            </div>
        </li>
    </div>
</template>

<style>
li {
    list-style-type: none;
}
</style>
