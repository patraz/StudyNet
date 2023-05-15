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
                    <form action="">
                        <div class="field">
                            <label for="">email</label>
                            <div class="control">
                                <input type="email" class="input">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Password</label>
                            <div class="control">
                                <input type="password" class="input">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Repeat Password</label>
                            <div class="control">
                                <input type="password" class="input">
                            </div>
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
  