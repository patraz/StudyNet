<template>
  
    <div class="signup">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">Sign Up</h1>
        </div>
      </div>

      <section class="section ">
        <div class="container">
            <div class="columns">
                <div class="column is-4 is-offset-4">
                    <form v-on:submit.prevent="submitForm">
                        <div class="field">
                            <label for="">email</label>
                            <div class="control">
                                <input type="email" class="input" v-model="username">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Password</label>
                            <div class="control">
                                <input type="password" class="input" v-model="password">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Repeat Password</label>
                            <div class="control">
                                <input type="password" class="input" v-model="password2">
                            </div>
                        </div>
                        <div class="notification is-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error"> {{ error }}</p>
                        </div>
                        <div class="field">
                            <div class="control">
                                <button class="button is-dark">sign up</button>
                            </div>
                        </div>
                    </form>

                   

                    <hr>

                    Or <router-link to="/login">click here to log in</router-link>
                </div>
            </div>
        </div>
      </section>
    </div>
</template>
  
<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    mounted(){
        document.title = 'Signup | StudyNet'
    },
    methods: {
        submitForm() {
            console.log('submitForm')

            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing!');
            }
            if  (this.password === '') {
                this.errors.push('The password is missing!');
            }
            if  (this.password !== this.password2) {
                this.errors.push('The passwords are not matching!');
            }
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                    .post('/api/v1/users/', formData)
                    .then(response => {
                        this.$router.push('/login')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something wemt wrong. Please try again')

                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>