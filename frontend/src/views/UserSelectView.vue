Vue.prototype.$hostname = 'http'

<script>
export default {
    name: "get-request",
    data() {
        return {
            users: {},
        };
    },
    created(){
        fetch("http://127.0.0.1:105/get_users")
        .then(response => response.json())
        .then(data => (this.users = data.users));
    }
};
</script>

<template>
  <div class="box">
    <h1>Select User</h1>
  </div>
  <div class = "li">
    <li v-for="( users , index) in users">
        <div class="box">
            <label class = "radio">
                <input type = "radio">
                Show
                <input type = "radio">
                Hide | 
                Toggle Data |
            </label>
                {{ users.first_name }} {{ users.last_name }}
        </div>
    </li>
 </div>
</template>

<style>
li{
    list-style-type: none;
}
</style>
