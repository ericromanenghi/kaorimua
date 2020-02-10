<template>
    <div class='container'>
        <div class='error'>
            <p>Sorry, couldn't load the page content. Please try again</p>
            <p><button @click='refreshPage'>Refresh page</button></p>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        refreshPage () {
            window.location = window.location.href
        }
    },
}
</script>

<style scoped lang='scss' src='@/scss/error.scss'></style>
