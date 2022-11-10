CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE `Reactions` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `label` varchar,
  `image_url` varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);


INSERT INTO `Users` VALUES (null, "Kristen", "Chandler", "krismchandler@gmail.com", "bio here", "kmchandler", "password", "https://img.freepik.com/premium-vector/cartoon-cute-funny-python-snake-jungle-tree_53500-462.jpg?w=2000", "2020-11-1",  "not active");
INSERT INTO `Users` VALUES (null, "Rochelle", "Rossman", "Rochelle.rossman@gmail.com", "bio here", "rrossman", "password", "https://img.freepik.com/premium-vector/cartoon-cute-funny-python-snake-jungle-tree_53500-462.jpg?w=2000", "2020-11-1",  "not active");
INSERT INTO `Users` VALUES (null, "Jacob", "Martin", "jmartin@gmail.com", "bio here", "jmartin", "password", "https://img.freepik.com/premium-vector/cartoon-cute-funny-python-snake-jungle-tree_53500-462.jpg?w=2000", "2020-11-1",  "not active");
INSERT INTO `Users` VALUES (null, "Sariah", "Campopiano", "scampopiano@gmail.com", "bio here", "scampopiano", "password", "https://img.freepik.com/premium-vector/cartoon-cute-funny-python-snake-jungle-tree_53500-462.jpg?w=2000", "2020-11-1",  "not active");
INSERT INTO `Users` VALUES (null, "Joel", "McAnulty", "jmcanulty@gmail.com", "bio here", "jmcanulty", "password", "https://img.freepik.com/premium-vector/cartoon-cute-funny-python-snake-jungle-tree_53500-462.jpg?w=2000", "2020-11-1",  "not active");


INSERT INTO `DemotionQueue` VALUES ("silly mistake", 1, 2);
INSERT INTO `DemotionQueue` VALUES ("used office microwave to heat fish", 2, 5);
INSERT INTO `DemotionQueue` VALUES ("leaves passive aggressive notes around office", 1, 3);
INSERT INTO `DemotionQueue` VALUES ("always whistles", 3, 2);


INSERT INTO `Subscriptions` VALUES (null, 3, 2, 2020-11-1);
INSERT INTO `Subscriptions` VALUES (null, 1, 5, 2020-11-1);
INSERT INTO `Subscriptions` VALUES (null, 2, 3, 2020-11-1);
INSERT INTO `Subscriptions` VALUES (null, 2, 4, 2020-11-1);


INSERT INTO `Posts` VALUES (null, 3, 2, "Learning Python", 2020-11-1, "https://img.freepik.com/premium-vector/cartoon-cute-funny-python-snake-jungle-tree_53500-462.jpg?w=2000", "message content", "approved");
INSERT INTO `Posts` VALUES (null, 1, 4, "Learning Python", 2020-11-1, "https://img.freepik.com/premium-vector/cartoon-cute-funny-python-snake-jungle-tree_53500-462.jpg?w=2000", "message content", "approved");
INSERT INTO `Posts` VALUES (null, 3, 3, "Learning Python", 2020-11-1, "https://img.freepik.com/premium-vector/cartoon-cute-funny-python-snake-jungle-tree_53500-462.jpg?w=2000", "message content", "approved");
INSERT INTO `Posts` VALUES (null, 2, 1, "Learning Python", 2020-11-1, "https://img.freepik.com/premium-vector/cartoon-cute-funny-python-snake-jungle-tree_53500-462.jpg?w=2000", "message content", "approved");




INSERT INTO `Comments` VALUES (null, 2, 4, "comment content");
INSERT INTO `Comments` VALUES (null, 2, 3, "comment content");
INSERT INTO `Comments` VALUES (null, 1, 2, "comment content");
INSERT INTO `Comments` VALUES (null, 4, 2, "comment content");


INSERT INTO `Reactions` VALUES (null, "smile", "https://www.pngfind.com/pngs/m/10-102223_download-slightly-smiling-emoji-icon-emojis-png-ios.png");
INSERT INTO `Reactions` VALUES (null, "frown", "http://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-12/256/frowning-face.png");
INSERT INTO `Reactions` VALUES (null, "clap", "https://www.pngitem.com/pimgs/m/12-129188_clapping-hands-emoji-png-graphic-free-clap-hands.png");
INSERT INTO `Reactions` VALUES (null, "cry", "https://images.emojiterra.com/google/android-11/512px/1f62d.png");
INSERT INTO `Reactions` VALUES (null, "laugh", "https://s3.amazonaws.com/media.mediapost.com/dam/cropped/2017/11/24/laughingemoji-560.JPEG");



INSERT INTO `PostReactions` VALUES (null, 1, 2, 3);
INSERT INTO `PostReactions` VALUES (null, 2, 3, 4);
INSERT INTO `PostReactions` VALUES (null, 3, 2, 1);


INSERT INTO `Tags` VALUES (null, "python");
INSERT INTO `Tags` VALUES (null, "django");
INSERT INTO `Tags` VALUES (null, "javascript");
INSERT INTO `Tags` VALUES (null, "react");
INSERT INTO `Tags` VALUES (null, "css");
INSERT INTO `Tags` VALUES (null, "html");


INSERT INTO `PostTags` VALUES (null, 1, 2);
INSERT INTO `PostTags` VALUES (null, 2, 3);
INSERT INTO `PostTags` VALUES (null, 3, 4);
INSERT INTO `PostTags` VALUES (null, 2, 1);
INSERT INTO `PostTags` VALUES (null, 4, 2);


INSERT INTO `Categories` VALUES (null, "python");
INSERT INTO `Categories` VALUES (null, "django");
INSERT INTO `Categories` VALUES (null, "javascript");
INSERT INTO `Categories` VALUES (null, "react");
INSERT INTO `Categories` VALUES (null, "css");
INSERT INTO `Categories` VALUES (null, "html");

SELECT
    a.id,
    a.label,
    a.image_url
FROM Reactions a

-- DELETE FROM PostReactions where id = 7
    c.id,
    c.author_id,
    c.post_id,
    c.content
FROM Comments c

SELECT
  u.id, 
  u.first_name,
  u.last_name,
  u.email,
  u.bio,
  u.username,
  u.password,
  u.profile_image_url,
  u.created_on,
  u.active
FROM Users u

SELECT
    p.id,
    p.user_id,
    p.category_id,
    p.title,
    p.publication_date,
    p.image_url,
    p.content,
    p.approved,
    c.label,
    u.first_name,
    u.last_name,
    u.username,
    u.profile_image_url
FROM Posts p
JOIN Users u on u.id = p.user_id
JOIN Categories c on c.id = p.category_id
WHERE p.user_id = 2

SELECT
            c.id,
            c.author_id,
            c.post_id,
            c.content,
            p.title,
            u.first_name,
            u.last_name,
            u.profile_image_url,
            u.username
        FROM Comments c
        JOIN Posts p
        ON p.id = c.post_id
        JOIN Users u
        ON u.id = c.author_id
        WHERE 
