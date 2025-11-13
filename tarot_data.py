# tarot_data.py

# DỮ LIỆU NỘI DUNG 78 LÁ BÀI TAROT (Major Arcana: 1-22, Minor Arcana: 23-78)
LUCKY_CONTENT = {
    # --- MAJOR ARCANA (22 Lá) ---
    1: "The Fool. Chúc mừng, ngày mới của bạn tràn đầy năng lượng. bạn sẽ được trải nghiệm những thử thách và cảm giác mới mẻ. Hãy cùng tận hưởng nguồn năng lượng mới tuôn chảy trong ngày của bạn và khiến nó thú vị! Vận mệnh: Khai phá",
    2: "The Magician. Ngày mới của bạn sẽ gắn liền với những hành động thiến thực. bạn sẽ trải qua một ngày mà chắc chắn phải vận dụng bổ não để tìm ra lối đi rồi.Vận mệnh: Vui vẻ",
    3: "The High Priestess. Nữ tư tế chính là tiềm thức của bạn. Hôm nay của bạn sẽ gắn liền với trực giác và giấc mơ. Những điều bạn bạn nghĩ, những cảm giác của bạn có lẽ sẽ đúng và mang lại cho bạn cảm giác tâm linh mạnh mẽ hôm nay. Vận mệnh: Kí ức",
    4: "The Empress. Nữ hoàng mang năng lượng màu mỡ, phì nhiêu. Cuộc sống của bạn hôm nay tràn đầy phước lành, niềm vui ấm áp, được bao bọc và có lẽ đầy tình cảm thiêng liêng của gia đình. Bà sẽ bảo vệ cho những người biết cho đi, biết trân trọng. Vận mệnh: Sinh sôi",
    5: "The Emperor. Hoàng đế mang tính răn đe và dạy dỗ. Ngày hôm nay bạn phải tuân thủ nghiêm ngặt quy định hoặc bị trừng phạt thích đáng. Sâu bên trong ông ấy sẽ dạy bạn những bài học quý giá và trưởng thành cho những kẻ tuân thủ.",
    6: "The Hierophant. Có lẽ hôm nay của bạn sẽ mở ra cho bạn vô số bài học mới, gặp gỡ để được học hỏi. Bạn sẽ được ôn ấy chỉ ra con đường đúng đắn để đi. Cẩn thận đừng để bị hìa tan! Vận mệnh: Tri thức",
    7: "The Lovers. Hôm nay có vẻ thần cupid đã mỉm cười với bạn, tình yêu tràn ngập thế gian. Hãy mỉm cười với anh ấy khi có thể nhé. Hôm nay có lẽ các mối quan hệ của bạ sẽ tiến triển nhiều đấy!",
    8: "The Chariot. Cỗ xe ở đây chứng tỏ bạn đã đi đúng hướng trong khì vọng của bạn để đạt được mục đích. Đừng suy nghĩ nữa, đây chính xác là lối bạn cần đi, nghe theo lý trí bạn, đừng nghe con tim. Hôm nay có lẽ bạn sẽ có nhiều tiến triển trong công việc.Vận mệnh: Săn bắn",
    9: "Strength. Hôm nay là một ngày tràn đầy năng lượng và nhiệt huyết của bạn. Sao bạn không bắt đầu ngày bằng một bài thể dục đơn giản hoặc hét lên để giải tỏa sức mạn của mình ra cho một ngày đầy tích cực nhỉ. Chú ý, đừng để dòng năng lượng của bạn thiêu rụi người khác.Vận mệnh: Bảo hộ",
    10: "The Hermit. Có vẻ như có gì đó khuất mắt và khiến bạn lạc lối trong suy nghĩ. Hôm nay hãy dành thật nhiều thời gian cho bản thân và đừng cố gắng bức tốc làm điều gì. Bạn cần chậm lại để suy ngẫm trước khi tiếp tục. Vận mệnh: Hư vô",
    11: "The Wheel Of Fortune. Vòng quay định mệnh đang quay. Hãy trân trọng những gì đến với bạn hôm nay như bạn sẽ không gặp lại nó lần nữa. Những gì bạn gieo mầm hôm nay vào vòng quay chính là những gì bạn gặt được trong tương lai. Vận mệnh: Cân bằng",
    12: "Justice. Có vẻ đã đến lúc phán xét những gì bạn làm trong quá khứ. Bạn không thể trốn tránh được nó và cô ta sẽ phán xét công tâm với thanh ươm của mình. Cẩn thận những vấn đề pháp lý! Vận mệnh: Trật tự",
    13: "The Hanged Man. Hôm nay là một ngày thú vị với bạn. Những chuyện thường ngày mà bạn nghĩ sẽ chỉ xảy ra theo hướng đó hôm nay có lẽ sẽ diễn ra theo một nhánh bất ngờ khác mà bạn không thể ngờ. Rằng bạn sẽ phải chấp nhận một cuộc sống với góc nhìn đa chiều, chấp nhận mọi chuyện đều có thể xảy ra và biết đâu bạn sẽ thấy nó thú vị.",
    14: "Death. Thần chết đã đến và bạn phải giao nộp quá khứ của mình. Những chuyện trong quá khứ, hãy khép cánh cửa đó lại và bắt đầu một chương hoàn toàn mới trong cuộc đời của bạn. Hôm nay một cánh cửa sẽ được đóng lại, một cái khác sẽ được mở ra.",
    15: "Temperance. Hôm nay là một ngày ổn định của bạn. Không vui, cũng không buồn. Bạn sẽ thấy sự hòa hợp xung quanh, hòa hợp các mối quan hệ, hòa hợp cảm xúc,... Hãy đón nhận 1 ngày êm dịu với vận mệnh Hòa Hợp. Vận mệnh: Hòa hợp",
    16: "The Devil. Con quỷ đã đến và mang theo sự cám dỗ đen tối khó cưỡn. ranh giới giữa thiện và ác mong manh như một sợi chỉ và chỉ đợi bạn quyết định. hãy nhớ một khi bạn dấn thân vào con đường của hắn, sẽ khó để thoát ra, cẩn thận với những cám dỗ hôm nay!!",
    17: "The Tower. Có vẻ nghiệp của bạn đã đạt max và bắt đầu đổ vỡ rồi. Cẩn thận những biến cố hôm nay, cẩn thận vận mệnh Hủy Diệt.",
    18: "The Star. Cô ấy là một ánh sao mang đến sự xoa dịu. Cô ấy không mang lại may mắn hay cơ hội. Cô ấy chỉ đến và mang lại cho bạn sự thoải mái, chấp nhận những quyết định và sự đổ vỡ, xoa dịu bạn để bạn dẫn chấp nhận hiện tại rằng nó đã xảy ra.",
    19: "The Moon. Mặt trăng mang đến những bí mật thầm kín và trực giác tâm linh. Hôm nay có lẽ bạn sẽ nghe được một bí mật động trời hoặc khó chịu với những tiếng thì thầm về bạn. Trạng thái của bạn cũng giống như thủy triều vào đêm trăng tròn vậy, không ổn định. đừng vội đưa ra kết luận và quyết định hôm nay. Vận mệnh: Thần bí",
    20: "The Sun. Chúc mừng bạn, thần may mắn đã mỉm cười với bạn rồi. Sao bạn không bắt đầu thức dậy và tận hưởng những điều may mắn và tích cực chờ đợi bạn hôm nay?",
    21: "Judgement. Hôm nay có lẽ bạn sẽ phải đưa ra nhiều quyết định quan trọng để rẽ cuộc đời, hãy suy nghĩ kĩ và chấp nhận sự thay đổi trong quyết định của bạn. Tiếng kèn cũng thông báo việc gieo nhân nào gặt quả nấy.",
    22: "The World. Bạn đang tiến dần đến việc hoàn thành 1 công việc, một sự án. Có lẽ hôm nay bạn sẽ dduoewcjxem kết quả và thành quả bạn đã gieo suốt thời gian qua. Vận mệnh: Chung mạc",

    # --- MINOR ARCANA (56 Lá) - Ví dụ đại diện ---
    # Wands (Gậy - Hành động, Sáng tạo)
    23: "Ace of Wands. Sự khởi đầu mới đầy năng lượng, đam mê và sáng tạo. Hãy hành động dứt khoát!",
    24: "Two of Wands. Lập kế hoạch và quyết định hướng đi trong tương lai. Cân nhắc lựa chọn.",
    25: "Three of Wands. Mở rộng tầm nhìn, hợp tác và chờ đợi thành quả từ nỗ lực trước đó.",
    26: "Four of Wands. Ăn mừng, hòa hợp, sự ổn định trong gia đình hoặc cộng đồng. Cảm giác an toàn.",
    27: "Five of Wands. Xung đột, cạnh tranh nhỏ, mâu thuẫn năng lượng. Hãy tìm cách hòa giải.",
    28: "Six of Wands. Chiến thắng công khai, thành công và được công nhận. Niềm tự hào.",
    29: "Seven of Wands. Bảo vệ lập trường, đối mặt với thử thách hoặc đối thủ. Sự kiên trì.",
    30: "Eight of Wands. Mọi việc diễn ra nhanh chóng, di chuyển hoặc nhận tin tức quan trọng.",
    31: "Nine of Wands. Phòng thủ, chuẩn bị cho trận chiến cuối cùng. Sự mệt mỏi nhưng kiên cường.",
    32: "Ten of Wands. Gánh nặng, trách nhiệm quá lớn. Hãy học cách chia sẻ bớt công việc.",
    33: "Page of Wands. Tin tức về những khởi đầu mới, sự khám phá, năng lượng trẻ trung.",
    34: "Knight of Wands. Hành động nhanh, phiêu lưu, thay đổi nơi ở hoặc kế hoạch đột ngột.",
    35: "Queen of Wands. Sự tự tin, độc lập, sức sống và sự tập trung vào sự nghiệp.",
    36: "King of Wands. Tầm nhìn xa, lãnh đạo bằng cảm hứng, sáng tạo và quyền lực.

    # Cups (Cốc - Cảm xúc, Mối quan hệ)
    37: "Ace of Cups. Sự khởi đầu của tình yêu, cảm xúc tích cực, lòng trắc ẩn và niềm vui.",
    38: "Two of Cups. Hợp tác, tình yêu lãng mạn, sự hòa hợp trong mối quan hệ.",
    39: "Three of Cups. Ăn mừng, tụ họp bạn bè, niềm vui và tình bằng hữu.",
    40: "Four of Cups. Thiếu động lực, không hài lòng với hiện tại, bỏ lỡ cơ hội vì thờ ơ.",
    41: "Five of Cups. Mất mát, đau buồn, hối tiếc về quá khứ mà bỏ qua những gì còn lại.",
    42: "Six of Cups. Ký ức về quá khứ, tuổi thơ, sự trong sáng, hoặc gặp lại người xưa.",
    43: "Seven of Cups. Lựa chọn ảo tưởng, nhiều sự lựa chọn nhưng thiếu thực tế. Cần tập trung.",
    44: "Eight of Cups. Rời bỏ một điều gì đó đã hoàn thành để tìm kiếm ý nghĩa sâu sắc hơn.",
    45: "Nine of Cups. Ước nguyện thành hiện thực, sự hài lòng và thỏa mãn về cảm xúc.",
    46: "Ten of Cups. Hạnh phúc trọn vẹn, gia đình viên mãn, niềm vui và hòa bình.",
    47: "Page of Cups. Tin tức lãng mạn, thông điệp về cảm xúc, sự mơ mộng và trực giác.",
    48: "Knight of Cups. Người mang lời đề nghị lãng mạn hoặc lời mời. Hành động theo cảm xúc.",
    49: "Queen of Cups. Đồng cảm, trực giác mạnh mẽ, yêu thương và hỗ trợ mọi người.",
    50: "King of Cups. Cân bằng cảm xúc, sự chín chắn, lòng trắc ẩn và sự bao dung.

    # Swords (Kiếm - Lý trí, Mâu thuẫn)
    51: "Ace of Swords. Sự sáng suốt, tư duy logic, sự thật phơi bày hoặc chiến thắng nhờ trí tuệ.",
    52: "Two of Swords. Bế tắc, từ chối nhìn nhận vấn đề, cần đưa ra quyết định khó khăn.",
    53: "Three of Swords. Đau buồn, phản bội, nỗi đau chia ly hoặc bị tổn thương cảm xúc.",
    54: "Four of Swords. Nghỉ ngơi, hồi phục, cần sự tĩnh lặng sau một thời gian căng thẳng.",
    55: "Five of Swords. Mất mát và thất bại, nhưng đôi khi là chiến thắng cay đắng. Xung đột.",
    56: "Six of Swords. Di chuyển, vượt qua khó khăn, hướng về tương lai tốt đẹp hơn.",
    57: "Seven of Swords. Lén lút, tự lừa dối bản thân hoặc người khác, hành động không minh bạch.",
    58: "Eight of Swords. Cảm thấy bị mắc kẹt, tự giới hạn bản thân bởi nỗi sợ hãi.",
    59: "Nine of Swords. Lo lắng, ác mộng, sợ hãi và mất ngủ. Cần đối diện với nỗi lo.",
    60: "Ten of Swords. Kết thúc đau đớn, sự tan vỡ hoàn toàn, nhưng cũng là điểm bắt đầu mới.",
    61: "Page of Swords. Sự tò mò, tin tức mới, hành động vội vàng và thiếu kinh nghiệm.",
    62: "Knight of Swords. Hành động bốc đồng, nhanh chóng nhưng thiếu kiên nhẫn. Sự xông xáo.",
    63: "Queen of Swords. Trí tuệ sắc bén, sự độc lập và thẳng thắn, nhưng đôi khi lạnh lùng.",
    64: "King of Swords. Tư duy logic, phân tích, công bằng và quyền lực dựa trên trí tuệ.

    # Pentacles (Tiền - Vật chất, Công việc)
    65: "Ace of Pentacles. Cơ hội mới về tài chính, công việc hoặc vật chất. Sự phồn thịnh.",
    66: "Two of Pentacles. Cân bằng giữa công việc và cuộc sống cá nhân, quản lý tài chính.",
    67: "Three of Pentacles. Hợp tác nhóm, làm việc cùng nhau để đạt được mục tiêu chung.",
    68: "Four of Pentacles. Tiết kiệm, giữ chặt tài sản, sợ hãi mất mát, có thể hơi keo kiệt.",
    69: "Five of Pentacles. Thiếu thốn, cảm giác bị loại trừ, khó khăn về tài chính hoặc sức khỏe.",
    70: "Six of Pentacles. Cho đi và nhận lại, từ thiện, chia sẻ của cải với người khác.",
    71: "Seven of Pentacles. Chờ đợi kết quả đầu tư, cần kiên nhẫn và đánh giá lại.",
    72: "Eight of Pentacles. Tập trung vào công việc, rèn luyện kỹ năng, sự tỉ mỉ.",
    73: "Nine of Pentacles. Độc lập tài chính, sự sung túc và thưởng thức thành quả lao động.",
    74: "Ten of Pentacles. Thịnh vượng lâu dài, di sản gia đình, sự ổn định về vật chất.",
    75: "Page of Pentacles. Cơ hội học tập, tin tức về tài chính hoặc công việc mới.",
    76: "Knight of Pentacles. Kiên trì, chậm rãi nhưng chắc chắn, tập trung vào nhiệm vụ.",
    77: "Queen of Pentacles. Nuôi dưỡng, sự xa hoa, an toàn tài chính, chăm sóc gia đình.",
    78: "King of Pentacles. Thành công tối cao về tài chính, sự giàu có và đáng tin cậy."
}
