<div class="container">
    <div class="page-header">
        <h1>List of news</h1>
    </div>

    <?php foreach ($news as $news_item): ?>

        <h2><?php echo $news_item['title'] ?></h2>
        <div id="main">
            <?php echo $news_item['text'] ?>
        </div>
        <p><a href="news/<?php echo $news_item['slug'] ?>">View article</a></p>

    <?php endforeach ?>
</div>