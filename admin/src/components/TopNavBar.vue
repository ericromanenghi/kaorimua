<template>
    <nav>
        <div class="container">
            <div class="nav-wrapper">
                <a href="#" class="brand-logo">{{ title }}</a>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
  name: 'TopNavBar',
  props: {
    title: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
