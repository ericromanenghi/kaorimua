<template>
    <div class='work__description' :style='{ backgroundImage: `url(${work.src})` }'>
        <div>
            <h2>{{ work.title }}</h2>
            <p>
                Model: {{ work.model }}<br>
                Photographer: {{ work.photographer }}<br>
                Make up: {{ work.makeup }}
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