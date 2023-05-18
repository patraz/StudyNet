<template>
    <nav class="navbar" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item is-size-4">StudyNet</router-link>
        </div>
        <div id="navbar-item" class="navbar-menu">
            <div class="navbar-start">
                <router-link to="/" class="navbar-item">Home</router-link>
                <router-link to="/about" class="navbar-item">About</router-link>
                <router-link to="/courses" class="navbar-item">Courses</router-link>
            </div>
            <div class="navbar-end">
                <div class="navbar-item">
                    <template v-if="$store.state.user.isAuthenticated">
                        <router-link :to="{name:'MyAccount'}" class="button is-info">My account</router-link>
                    </template>
                    <template v-else>
                        <div class="buttons">
                            <router-link to="/signup" class="button is-primary"><strong>Sign up</strong></router-link>
                            <router-link to="/login" class="button is-light"><strong>Log in</strong></router-link>
                        </div>
                    </template>
                    
                </div>
            </div>
        </div>
    </nav>
</template>
