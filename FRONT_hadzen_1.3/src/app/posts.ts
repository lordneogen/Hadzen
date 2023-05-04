import {Comment, comments} from "./comments";

export interface Post {
  title: string;
  content: string;
  img: string
  chanel: string;
  likes:number;
  date:Date;
  comments: Comment[];
}

export const posts = [
  {
    title: '5 способов повысить продуктивность работы',
    content: 'Работа — не всё, но мы проводим на ней большую часть своей жизни. Как же быть продуктивным и эффективным в работе? В этой статье мы расскажем вам 5 способов повысить продуктивность работы.',
    img: 'https://example.com/images/work.jpg',
    chanel: 'Productivity Life',
    likes: 23,
    date: new Date('2022-04-23T12:30:00'),
    comments: comments
  },
  {
    title: 'Рецепт пирога с яблоками',
    content: 'Наш любимый рецепт пирога с яблоками! Это очень простой рецепт, который пригодится каждому, кто любит сладкое.',
    img: 'https://example.com/images/apple-pie.jpg',
    chanel: 'Кулинарный блог',
    likes: 16,
    date: new Date('2022-04-22T10:00:00'),
    comments: [
      {
        user: 'Иван Иванов',
        text: 'Отличная статья! Очень интересно читать и узнавать новое.',
        date: new Date('2022-04-23T10:30:00'),
        like: 10,
        dis: 2,
      },
    ]
  },
  {
    title: 'Как путешествовать с детьми: советы опытной мамы',
    content: 'Путешествовать с детьми — это всегда приключение! Но как сделать его максимально комфортным и безопасным для всех участников? В этой статье опытная мама поделится своими советами и расскажет о своих опыте путешествий с детьми.',
    img: 'https://example.com/images/family-travel.jpg',
    chanel: 'Мамин блог',
    likes: 37,
    date: new Date('2022-04-20T15:45:00'),
    comments: [
      {
        user: 'Петр Сидоров',
        text: 'Очень интересно и познавательно! Большое спасибо автору за статью.',
        date: new Date('2022-04-21T09:15:00'),
        like: 2,
        dis: 0,
      },
    ]
  },
]
