
Maid.rules do

  rule 'move 2019 journal files into folder' do
    move(dir('~/Documents/Journal/2019*.markdown'), '~/Documents/Journal/2019')
  end

  rule 'move Benefit Wallet files into folder' do
    move(dir('~/Scans/Benefit Wallet Receipt*.pdf'), '/home/wadeallen/Documents/Receipts/Medical/Benefit_Wallet')
  end

  rule 'move Thrivent Credit Union into folder' do
    move(dir('~/Scans/Thrivent Credit Union*.pdf'), '/home/wadeallen/Documents/Statements/Thrivent Credit Union')
  end

  rule 'move Ball State Credit Union into folder' do
    move(dir('~/Scans/Ball State Credit Union*.pdf'), '/home/wadeallen/Documents/Receipts/Ball State Credit Union')
  end

  rule 'move Hooser Healthwise into folder' do
    move(dir('~/Scans/Levi Hoosier Healthwise*.pdf'), '/home/wadeallen/Documents/Receipts/Insurance/Health Insurance/Hoosier Healthwise')
  end

  rule 'move Forum Credit Union into folder' do
    move(dir('~/Scans/Forum Credit Union*.pdf'), '/home/wadeallen/Documents/Statements/Forum Credit Union')
  end

  rule 'move Teachers Credit Union into folder' do
    move(dir('~/Scans/Teachers Credit Union*.pdf'), '/home/wadeallen/Documents/Statements/Teachers Credit Union')
  end

  rule 'move Evansville Teachers Credit Union into folder' do
    move(dir('~/Scans/Evansville Teachers Credit Union*.pdf'), '/home/wadeallen/Documents/Statements/Evansville Teachers Credit Union')
  end

  rule 'move Teachers Credit Union into folder' do
    move(dir('~/Scans/Teachers Credit Union*.pdf'), '/home/wadeallen/Documents/Statements/Teachers Credit Union')
  end

  rule 'move Three Rivers Credit Union into folder' do
    move(dir('~/Scans/Three Rivers Credit Union*.pdf'), '/home/wadeallen/Documents/Statements/Three Rivers Credit Union')
  end

  rule 'move reminder call sheets into folder' do
    move(dir('~/Scans/*Nursery Reminder Calls.pdf'), '~/Documents/Administration/Nursery/Reminder Calls')
  end
  
  rule 'move nursery sign in sheets into folder' do
    move(dir('~/Scans/*Nursery Worker Sign In Sheet.pdf'), '/home/wadeallen/Documents/Administration/Nursery/Sign In Sheets')
  end

  rule 'move Macys Statement into folder' do
    move(dir('~/Scans/Macys Statement*.pdf'), '~/Documents/Statements/Macys')
  end

  rule 'move giving reports into folder' do
    move(dir('~/Scans/*Giving Report.pdf'), '~/Documents/Administration/Giving Reports')
  end

  rule 'move benefit wallet receipts into folder' do
    move(dir('~/Scans/Benefit Wallet*.pdf'), '~/Documents/Receipts/Medical/Benefit Wallet Receipts')
  end

  rule 'move church receipts into folder' do
    move(dir('~/Scans/*Church Receipt*.pdf'), '~/Documents/Receipts/Church/Current')
  end

  rule 'move housing receipts into folder' do
    move(dir('~/Scans/*Housing Receipt*.pdf'), '~/Documents/Receipts/Housing/Misc Housing')
  end

  rule 'move Comcast Bill into folder' do
    move(dir('~/Desktop/Comcast Bill*.pdf'), '~/Documents/Receipts/Housing/Comcast')
  end

  rule 'move Kohls Statement into folder' do
    move(dir('~/Scans/Kohls Statement*.pdf'), '~/Documents/Statements/Kohls')
  end

  rule 'move American Eagle Statement into folder' do
    move(dir('~/Scans/American Eagle Statement*.pdf'), '~/Documents/Statements/American Eagle')
  end

  rule 'move Indiana Michigan Power Statement into folder' do
    move(dir('~/Scans/I&MBill_*.pdf'), '~/Documents/Receipts/Housing/Utilities/Electric')

  rule 'move School Receipts into folder' do
    move(dir('~/Scans/*School Receipt*.pdf'), '~/Documents/Receipts/School')
  end

  rule 'move Yorktown Muncipal Utilities into folder' do
    move(dir('~/Scans/Yorktown Municipal Utilities*.pdf'), '~/Documents/Receipts/Housing/Utilities/Water')
  end

  rule 'move Maurices Statement into folder' do
    move(dir('~/Scans/Maurices*.pdf'), '~/Documents/Statements/Maurices')
  end

  rule 'move Target Statement into folder' do
    move(dir('~/Scans/Target Card*.pdf'), '~/Documents/Receipts/Target')
  end

  rule 'move Anna Vanderbilt Health Insurance Statement into folder' do
    move(dir('~/Scans/Anna Vanderbilt Health Insurance*.pdf'), '~/Documents/Anna/Anna_Vanderbilt')
  end

  rule 'move New York and Company Statement into folder' do
    move(dir('~/Scans/New York and Company*.pdf'), '~/Documents/Receipts/New York and Company')
  end

  rule 'move TJ Maxx Statement into folder' do
    move(dir('~/Scans/TJ Maxx Statement*.pdf'), '~/Documents/Receipts/TJ Maxx')
  end

  rule 'move Victoria Secret Statement into folder' do
    move(dir('~/Scans/Victoria Secret Statement*.pdf'), '~/Documents/Receipts/Victoria Secret')
  end

  rule 'move Childrens Place Statement into folder' do
    move(dir('~/Scans/Childrens Place Statement*.pdf'), '~/Documents/Receipts/Childrens Place')
  end

  rule 'move ATT Statement into folder' do
    move(dir('~/Desktop/ATT_Bill_*.pdf'), '~/Documents/Receipts/Wireless Phone')
  end

  rule 'move IU Health Statement into folder' do
    move(dir('~/Scans/IU Health Insurance*.pdf'), '~/Documents/Receipts/Insurance/Health Insurance/IU Health Insurance')
  end

  rule 'move CareSource Statement into folder' do
    move(dir('~/Scans/CareSource*.pdf'), '~/Documents/Receipts/Insurance/CareSource')
  end

  rule 'move MD Wise Statement into folder' do
    move(dir('~/Scans/MD Wise*.pdf'), '~/Documents/Receipts/Insurance/Health Insurance/MD Wise Wade Christy')
  end

  rule 'move Vectren Bill into folder' do
    move(dir('~/Scans/Vectren*.pdf'), '~/Documents/Receipts/Housing/Utilities/Gas')
  end

  end
end


