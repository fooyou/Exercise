/*
* @Author: Joshua Liu
* @Date:   2017-11-02 17:05:33
* @Last Modified by:   liuchaozhen
* @Last Modified time: 2017-11-02 17:07:44
*/
CREATE TABLE entries (
    id INT AUTO_INCREMENT,
    title TEXT,
    content TEXT,
    posted_on DATETIME,
    primary key (id)
);
