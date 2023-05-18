<template>
    <div class="about">
      <div class="hero is-info is-medium">
        <div class="hero-body has-text-centered">
          <h1 class="title">My Account</h1>
        </div>
      </div>
      <section class="section has-text-centered">
        <button @click="logout()" class="button is-danger">logout</button>
      </section>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    methods: {
        async logout() {
            console.log('logout')
            await axios
              .post('/api/v1/token/logout/')
              .then(response => {
                console.log("logged out")
              })
              
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}

</script>