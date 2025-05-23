# HoMemeTown Dr. CareSam 시스템 아키텍처

## 🏗️ 전체 시스템 구조

### Frontend Development
- **React.js** framework for responsive user interface
- **Material-UI** component library for consistent design
- **WebSocket** implementation for real-time chat functionality
- **Client-side-only** session management with no persistent storage

### Backend Infrastructure
- **Node.js** runtime environment with **Express.js** framework
- **Stateless architecture** with no database implementation
- **Direct API integration** with OpenAI's GPT-4
- **Nginx reverse proxy** for load balancing

### OpenAI API Integration
- **GPT-4 API** with custom prompt engineering
- **No retention** of conversation history
- **Independent sessions** for each interaction
- **Response token limiting** for cost optimization
- **Regular monitoring** of API performance and reliability

## 📊 Service Flow Architecture
Figure 1 illustrates the service flow architecture of the
HoMemeTown chatbot. The architecture depicts the user’s
journey, starting from the login process through the user
interface on their PC. After logging in, users can access the
gratitude journal section, where they can find a guide on “How
to write gratitude journal” and proceed to write their own entries
[13]. The system assigns a unique session number to each
journaling session and securely saves the user’s journal entries
along with metadata such as the gratitude journal count, detected
tokens or keywords, expressed emotions, and word count [14].
Users are rewarded with token rewards upon completing a
journal entry, and the system generates a personalized response
acknowledging their entry [4]. They can then continue their
gratitude practice by initiating a new chat through the “CareSam:
Talk to a friend” option. This feature allows users to select an
emotion from a set of 25 emotional icons and provide more
context about their feelings. Cowen and Keltner’s [15] research
on emotional classification inspired the inclusion of these icons.
Recognizing these 25 unique emotions can help users cultivate
greater self-awareness and sensitivity toward others, leading to
increased empathy, connection, and understanding.
The HoMemeTown chatbot aims to encourage and motivate
users to cultivate gratitude practice by providing a seamless
user flow, personalized responses, and emotional attunement.
The HoMemeTown chatbot is currently accessible as an open
web application. This pilot version is available for public testing,
allowing anyone to interact with the chatbot and experience its
features firsthand. The chatbot’s continued operation
demonstrates our commitment to transparency and ongoing
exploration of digital mental health interventions. This open
access approach enhances research reproducibility and provides
opportunities for continuous feedback and improvement.

## 🎭 Emotional Recognition System
Figure 2 displays the 25 emotional icons used in the
HoMemeTown chatbot. Inspired by Microsoft’s emotion
monsters, these icons represent a wide range of human emotions,
allowing users to select one that reflects their current mood.
This selection facilitates a more personalized and emotionally
attuned response from the chatbot. 
![Fig 1(rev)](https://github.com/user-attachments/assets/ef65c765-d943-45a3-9446-39650c37a4ac)
![Fig2](https://github.com/user-attachments/assets/809b2d69-5387-45b1-9201-7e0a18e89666)


