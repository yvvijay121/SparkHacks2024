import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const userAccountStore = defineStore('user_account', () => {
  const userAccount = ref({
    username: 'johndoe'
  })

  return {
    userAccount,
  }
})
