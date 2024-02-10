script>
export default {
    name: "get-request",
    data() {
        return {
            users: [],
        };
    },
    created(){
        fetch("http://127.0.0.1:105/get_users")
        .then(response => response.json())
        .then(data => (this.users.users[0] = data))
    }
};
</script>

<template>
  <div class="box">
    <h1>Select User</h1>
  </div>
  <div class="box">
    <label class = "radio">
        <input type = "radio">
        Toggle Data |
    </label>
    <br>
    {{ users.first_name }}
  </div>
</template>
