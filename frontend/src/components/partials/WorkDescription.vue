<template>
    <div class='work__description'>
        <div>
            <h2>{{ work.name }}</h2>
            <p>
                <span v-if='work.model'>Model: {{ work.model }}<br></span>
                <span v-if='work.photographer'>Photographer: {{ work.photographer }}</span>
            </p>
        </div>
    </div>
</template>

<script>
export default {
    props: [ 'work' ],

}
</script>

<style lang='scss' src='@/scss/work/description.scss'></style>