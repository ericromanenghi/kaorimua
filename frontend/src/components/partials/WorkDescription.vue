<template>
    <div class='work__description'>
        <div>
            <h2>{{ work.name }}</h2>
            <p>
                Model: {{ work.model }}<br>
                Photographer: {{ work.photographer }}
            </p>
        </div>
    </div>
</template>

<script>
export default {
    props: [ 'work' ],

}
</script>

<style lang='scss' src='@/scss/work/description.scss' scoped></style>