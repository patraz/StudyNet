<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to StudyNet</h1>
        <h2 class="Subtitle">Learn what you want</h2>
      </div>
    </div>
    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-clock"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study at your own pace</h2>

              <p>Lorem Ipsum </p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-comments"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study at your own pace</h2>

              <p>Lorem Ipsum </p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="fas fa-home"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study from your home</h2>

              <p>Lorem Ipsum </p>
            </div>
          </div>
          <div class="column is-12 has-text-centered">
            <a href="/signup" class="button is-info is-size-3 mt-6 mb-6">Click to get started</a>
          </div>

          <hr>

          <div 
              class="column is-3"
              v-for="course in courses"
              v-bind:key="course.id"
          >
            <CourseItem :course="course"/>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import CourseItem from '@/components/CourseItem.vue'

export default {
  name: 'HomeView',
  data() {
        return {
            courses: []
        }
    },
    components: {
        CourseItem,
    },
    mounted() {
        console.log('mounted')

        axios
            .get('/api/v1/courses/get_frontpage_courses/')
            .then(response => {
                console.log(response.data)
                this.courses = response.data
            })

        document.title = 'Welcome | StudyNet'

    }

}
</script>
